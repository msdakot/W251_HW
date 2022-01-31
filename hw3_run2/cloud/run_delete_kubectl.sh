kubectl delete deployment cloud-mosquitto-deployment
kubectl delete deployment cloud-listener
kubectl delete service cloud-mosquitto-service

sudo systemctl stop k3s

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)