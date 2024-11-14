#!/bin/python3
# -*- encoding: utf-8 -*-
# Получить данные с mqtt в zabbix.
#_version__ = YYYYMMDDhhmm
__version__ = 202411141825

from paho.mqtt import subscribe, client as mqtt # pip install paho-mqtt
from multiprocessing import Process, Queue
from time import sleep
import json, sys
class get_branch:
    def __init__(self, set: dict = {'host':'127.0.0.1'}, subscribe='$SYS/#', wait: int = 3, alldata: bool = False):
        self.set = set
        self.subscribe = subscribe
        self.len =  len(subscribe.split('/'))
        self.wait = wait
        self.alldata = alldata
        self.mqtt_data = {}
    def on_connect(self,client, userdata, flags, reason_code, properties):
        client.subscribe(self.subscribe)
    def on_message(self,client, userdata, msg):
        global mqtt_data
        if self.alldata:
            self.mqtt_data.update({msg.topic: msg.payload})
        else:
            if len(msg.topic.split('/')) == self.len:
                self.mqtt_data.update({msg.topic: msg.payload})
        #print('MQTT =>', len(mqtt_data), mqtt_data)
        if self.queue.empty() == False:
            self.queue.get(self.mqtt_data)
        self.queue.put(self.mqtt_data)
    def run_mqtt_cli(self):
        mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        mqttc.connect(**self.set)
        mqttc.loop_forever()
    def run(self):
        self.queue = Queue()
        prc = Process(target=self.run_mqtt_cli, args=())
        prc.start()
        sleep(self.wait)
        if not self.queue.empty():
            mqtt_data = self.queue.get()
        prc.kill()
        self.queue.close()
        return mqtt_data

if __name__ == '__main__':
    name, req = sys.argv
    req = req.replace("'", '"')
    req = json.loads(req)
    subscribe = req.pop('subscribe')
    set = req
    mqtt_data = get_branch(set, subscribe=subscribe).run()
    branch = subscribe.split('/#')[0]
    ret = {}
    for el in mqtt_data:
        ret.update({el.split(branch)[1][1:]: str(mqtt_data[el], encoding='utf-8')})
    print(json.dumps(ret))

