
#  CEILING FAN MQTT CONTROL #


Control your ceiling fans via MQTT


:::CLIENT INFO:::


You must have mosquitto installed on the server running the fan-control code.
*sudo apt-get install mosquitto*


Make sure python3 is installed.

Make pip3 is installed: 
*sudo apt-get install python3-pip*

Make sure that gpiozero, rpi.gpio and paho-mqtt are installed via pip3
*sudo pip3 install gpizero rpi.gpio paho-mqtt*

To execute fan-control.py, run it:
```/usr/bin/python3 fan-control.py```

To start quietly in the backgroup, use:
```nohup /usr/bin/python3 ./fan-control.py &```

Also, to have the script run at boot, I created a System Service. See fancontrol.service

Add file to /etc/systemd/system/ directory

Then run ```sudo systemctl enable fancontrol.service```

Currently having issues with not connecting to broker as service. Possibly due
to the slowness of the raspberry pi 1. Need to investigate. 

```pi@raspberrypi:~ $ systemctl status fancontrol.service
● fancontrol.service - Fan Control Python Script
   Loaded: loaded (/etc/systemd/system/fancontrol.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since Mon 2018-12-10 07:02:54 GMT; 50s ago
  Process: 322 ExecStart=/usr/bin/python3 /home/pi/fan-control.py (code=exited, status=1/FAILURE)
 Main PID: 322 (code=exited, status=1/FAILURE)

Dec 10 07:02:53 raspberrypi python3[322]:   File "/home/pi/.local/lib/python3.5/site-packages/paho/mqtt/client.py", line 962, in reconnect
Dec 10 07:02:53 raspberrypi python3[322]:     sock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))
Dec 10 07:02:53 raspberrypi python3[322]:   File "/usr/lib/python3.5/socket.py", line 712, in create_connection
Dec 10 07:02:53 raspberrypi python3[322]:     raise err
Dec 10 07:02:53 raspberrypi python3[322]:   File "/usr/lib/python3.5/socket.py", line 703, in create_connection
Dec 10 07:02:53 raspberrypi python3[322]:     sock.connect(sa)
Dec 10 07:02:53 raspberrypi python3[322]: OSError: [Errno 113] No route to host
Dec 10 07:02:54 raspberrypi systemd[1]: fancontrol.service: Main process exited, code=exited, status=1/FAILURE
Dec 10 07:02:54 raspberrypi systemd[1]: fancontrol.service: Unit entered failed state.
Dec 10 07:02:54 raspberrypi systemd[1]: fancontrol.service: Failed with result 'exit-code'.
```
If I manually run ```sudo systemctl start fancontrol.service``` it will load fine...

:::BROKER INFO:::

on the broker(the machine giving the orders), you must have mosquitto-clients installed
*sudo apt-get install mosquitto-clients*

from broker, you can run this command to send signal/message to the pi running fan-control.py

```mosquitto_pub -h 10.0.201.101 -t pizza -k 60 -m "living room fan low"```

Don't forget firewall rules. TCP 1883



----

---

For systemd help, see these findings that helped me:
https://raspberrypi.stackexchange.com/questions/84892/run-python-script-at-startup-with-systemd-service
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-unit_files
https://unix.stackexchange.com/questions/126009/cause-a-script-to-execute-after-networking-has-started

It restart service on failure, looking into:
https://singlebrook.com/2017/10/23/auto-restart-crashed-service-systemd/