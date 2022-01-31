sudo systemctl start k3s
kubectl apply -f cloud_broker/deployment.yaml
kubectl apply -f cloud_broker/service.yaml
kubectl apply -f cloud_logger/cloud_logger.yaml

kubectl get service

sleep 10

kubectl get pods
