eval $(minikube -p minikube docker-env)
docker build --no-cache -t service1-k8s:latest .
