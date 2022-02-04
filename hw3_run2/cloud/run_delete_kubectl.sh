kubectl delete deployment cloud-mosquitto-deployment
kubectl delete deployment image-processor-deployment
kubectl delete service cloud-mosquitto-service

sudo systemctl stop k3s

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
