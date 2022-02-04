sudo systemctl start k3s

kubectl apply -f mqtt_broker/deployment.yaml
kubectl apply -f mqtt_broker/service.yaml
kubectl apply -f mqtt_message_logger/logger_deployment.yaml
kubectl apply -f mqtt_message_forwarder/forwarder_deployment.yaml
kubectl apply -f face_detection/face_detection.yaml
kubectl get service

sleep 10

kubectl get pods
