## MQTT -(json)-> Zabbix
Получить ветку из mqtt в zabbix в json формате.<br>
копируем файл get_branch.py в директорию /usr/lib/zabbix/externalscripts<br>
делаем его исполняемым<br>
```
chmod +x /usr/lib/zabbix/externalscripts/get_branch.py
```
Получить данные из MQTT WirenBoard <br>
Создать элемент данных
![](https://github.com/VBCRFV/zabbix/blob/main/readme/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.png)
Провести тест
![](https://github.com/VBCRFV/zabbix/blob/main/readme/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%2C%20%D1%82%D0%B5%D1%81%D1%82.png)
Создать зависимый элемент данных
![](https://github.com/VBCRFV/zabbix/blob/main/readme/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%2C%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D0%B9.png)

![](https://github.com/VBCRFV/zabbix/blob/main/readme/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%2C%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D0%B9%2C%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20.png)
