import paho.mqtt.client as mqtt
  

LOCAL_MQTT_HOST = "cloud-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_detection"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  print("each captured frame is how many bytes:")
  try:
    print("message received (bytes): ",len(msg.payload))
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)
local_mqttclient.on_message = on_message


# go into a loop
local_mqttclient.loop_forever()