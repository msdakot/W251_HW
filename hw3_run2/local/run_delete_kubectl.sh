kubectl delete deployment cli-mosquitto-deployment
kubectl delete deployment face_finder
kubectl delete deployment cli-listener
kubectl delete service cli-mosquitto-service

sudo systemctl stop k3s

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)