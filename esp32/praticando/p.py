import network
from time import sleep
from umqttsimple import MQTTClient
import ssl
import time
import machine

rede = network.WLAN(network.STA_IF)
rede.active(True)
print(rede.scan())
rede.connect('Lab', '123456789')
while not (rede.isconnected()):
    print(".", end="")
    sleep(1)
print(rede.ifconfig())

mqtt_server = b'4166df98726c4a0cb6bcbd279ddc281a.s1.eu.hivemq.cloud'
port = 8883


user = b"cotuca"
pwd = b"cotuca"
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b"aula_not"

try:
    client = MQTTClient(
        client_id.
        mqtt_server,
        port,
        user,
        password,
        ssl = True,
        ssl_params = {"server_hostname": mqtt_server}
    )
    
    client.connect()
    print("Connected...")
except OSError as e:
    print(e)
    sleep(5)
    machine.reset()
    
deadline = time.ticks_add(time.ticks_ms(), 5000)

while True:
=    if time.ticks_diff(deadline, time.ticks_ms()) < 0:
        tempo = time.ticks_ms()
        msg = b'{"tempo": %0.2f }' % tempo
        client.publish(topic_pub, msg)
        deadline = time.ticks_add(time.ticks_ms(), 50000)