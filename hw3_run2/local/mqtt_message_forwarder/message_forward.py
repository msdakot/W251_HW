import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST = "cli-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_detection" 

REMOTE_MQTT_HOST = "172.31.92.225"
REMOTE_MQTT_PORT = 30003
REMOTE_MQTT_TOPIC = "face_detection"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode("utf-8")))
    
    # Establish Remote connection
    print('Connecting to remote...')


    remote_mqttclient = mqtt.Client()
    remote_mqttclient.on_connect = on_connect_remote
    remote_mqttclient.connect(REMOTE_MQTT_HOST, port=30003, keepalive=60)

    # Forward Message
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

print('Connecting to local host...')
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)

local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
