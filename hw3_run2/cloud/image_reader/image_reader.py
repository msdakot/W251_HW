import numpy as np
import cv2
import paho.mqtt.client as mqtt
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from aws_creds import aws_access_key_id, aws_secret_access_key


LOCAL_MQTT_HOST = "cloud-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_detection"

BUCKET = 'w251-dhruvi'

#S3 Connection
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
	

def on_message(client,userdata, msg):
    try:
        print("message received")
        # get payload
        img = msg.payload

        # Generate File Name
        date_time = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
        file_name = str(date_time) + '_image.png'

        # Save Image
        nparr = np.frombuffer(img, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite(file_name, img)
        
        try:
            # Upload Image 
            s3.upload_file(file_name, BUCKET, "HW3/{}".format(str(file_name)))
            print('wrote file name: ', file_name)
        except ClientError as e:
            print(e)

    except:
        print("Unexpected error:", sys.exc_info()[0])

print("connecting to local network")
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
