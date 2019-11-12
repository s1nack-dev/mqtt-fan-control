
from gpiozero import *
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import time

remote_power = OutputDevice(10) # master controller
fan_low = OutputDevice(17) # gpio4  - new 17
fan_med = OutputDevice(11) # gpio17 - new 27
fan_high = OutputDevice(22) # gpio18 - new 22
fan_off = OutputDevice(18) # gpio27 - new 18
light = OutputDevice(4) # gpio22 - new 4

dip1 = OutputDevice(23) # gpio5 - new 23
dip2 = OutputDevice(24) # gpio6 - new 24
dip3 = OutputDevice(25) # gpio12 - new 25 
dip4 = OutputDevice(8) # gpio13 - new 08

remote_power.off()
fan_low.off()
fan_med.off()
fan_high.off()
light.off()
dip1.off()
dip2.off()
dip3.off()
dip4.off()


# Used for debugging #
'''fan_low = 'fan_low'
fan_med = 'fan_med' 
fan_high = 'fan_high' 
fan_off = 'fan_off' 
light = 'light' 

dip1 = 'dip1'
dip2 = 'dip2'
dip3 = 'dip3'
dip4 = 'dip4' '''

#dip_cleared = none


#fan_select

room = []

# living room  dip4
# office dip1 dip2
# master none 
# wardrobe  dip1

# Assisted by: https://www.eclipse.org/paho/clients/python/docs/
# Also youtube video: https://www.youtube.com/watch?v=QAaXNt0oqSI



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection, returned code=",rc)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/ceilingfans")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # This prints topic and message payload
    print(msg.topic+" "+str(msg.payload))
    
    # This prints message payload with stripped formatting
    print(str(str(msg.payload).replace("b", "")).replace("'", ""))

    # This saves stripped payload message as a variable
    message = (str(str(msg.payload).replace("b", "")).replace("'", ""))
    
    remote_power.on()
    
    # living room
    if message == "living room light":
        print("living room light")
        dip4.on()
        light.on()
        time.sleep(.5)
        light.off()
        time.sleep(.5)
        dip4.off()
    elif message == "living room fan low":
        print("living room fan low")
        dip4.on()
        fan_low.on()
        time.sleep(1)
        fan_low.off()
        time.sleep(1)
        dip4.off()
    elif message == "living room fan med":
        print("living room fan med")
        dip4.on()
        fan_med.on()
        time.sleep(.5)
        fan_med.off()
        time.sleep(.5)
        dip4.off()
    elif message == "living room fan high":
        print("living room fan high")
        dip4.on()
        fan_high.on()
        time.sleep(.5)
        fan_high.off()
        time.sleep(.5)
        dip4.off()
    elif message == "living room fan off":
        print("living room fan off")
        dip4.on()
        fan_off.on()
        time.sleep(.5)
        fan_off.off()
        time.sleep(.5)
        dip4.off()
    
    # Master Room
    elif message == "master light":
        print("master light")
        dip1.off()
        dip2.off()
        dip3.off()
        dip4.off()
        light.on()
        time.sleep(.5)
        light.off()
        time.sleep(.5)
    elif message == "master fan low":
        print("master fan low")
        fan_low.on()
        time.sleep(.5)
        fan_low.off()
        time.sleep(.5)
    elif message == "master fan med":
        print("master fan med")
        fan_med.on()
        time.sleep(.5)
        fan_med.off()
        time.sleep(.5)
    elif message == "master fan high":
        print("master fan high")
        fan_high.on()
        time.sleep(.5)
        fan_high.off()
        time.sleep(.5)
    elif message == "master fan off":
        print("master fan off")
        fan_off.on()
        time.sleep(.5)
        fan_off.off()
        time.sleep(.5)

    # Closet Room
    elif message == "closet room light":
        print("closet room light")
        dip1.on()
        light.on()
        time.sleep(.5)
        light.off()
        time.sleep(.5)
        dip1.off()
    elif message == "closet room fan low":
        print("closet room fan low")
        dip1.on()
        fan_low.on()
        time.sleep(.5)
        fan_low.off()
        time.sleep(.5)
        dip1.off()
    elif message == "closet room fan med":
        print("closet room fan med")
        dip1.on()
        fan_med.on()
        time.sleep(.5)
        fan_med.off()
        time.sleep(.5)
        dip1.off()
    elif message == "closet room fan high":
        print("closet room fan high")
        dip1.on()
        fan_high.on()
        time.sleep(.5)
        fan_high.off()
        time.sleep(.5)
        dip1.off()
    elif message == "closet room fan off":
        print("closet room fan off")
        dip1.on()
        fan_off.on()
        time.sleep(.5)
        fan_off.off()
        time.sleep(.5)
        dip1.off()
    
    # Office
    elif message == "office light":
        print("office light")
        dip1.on()
        dip2.on()
        light.on()
        time.sleep(.5)
        light.off()
        time.sleep(.5)
        dip1.off()
        dip2.off()
    elif message == "office fan low":
        print("office fan low")
        dip1.on()
        dip2.on()
        fan_low.on()
        time.sleep(.5)
        fan_low.off()
        time.sleep(.5)
        dip1.off()
        dip2.off()
    elif message == "office fan med":
        print("office fan med")
        dip1.on()
        dip2.on()
        fan_med.on()
        time.sleep(.5)
        fan_med.off()
        time.sleep(.5)
        dip1.off()
        dip2.off()
    elif message == "office fan high":
        print("office fan high")
        dip1.on()
        dip2.on()
        fan_high.on()
        time.sleep(.5)
        fan_high.off()
        time.sleep(.5)
        dip1.off()  
        dip2.off()
    elif message == "office fan off":
        print("office fan off")
        dip1.on()
        dip2.on()
        fan_off.on()
        time.sleep(.5)
        fan_off.off()
        time.sleep(.5)
        dip1.off()
        dip2.off()

    else:
        print("Unknown Message") 

    remote_power.off()

#def message_action():
#    message1 = on_message
#    print("message action print " +str(message1))
#    if message1 == "pizza":
#        print("Prepare cooking")
#    else:
#        print("standby")    
    
def on_log(client, userdata, level, buf):
    print("log: "+buf)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.message_action = message_action
client.on_log = on_log

client.connect("mqtt_broker_ipaddress_goes_here", 1883, 60)
client.username_pw_set("mqtt_username", "mqtt_password")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# Call one of the loop*() functions to maintain network traffic flow with the broker
client.loop_forever()

#client.username_pw_set("mqtt_user", "PASSWORD")
 