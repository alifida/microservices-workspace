kubectl delete -f service1-deployment.yaml
kubectl apply -f service1-deployment.yaml
kubectl apply -f service1-service.yaml

kubectl rollout restart deployment/service1-deployment
kubectl apply -f service1-service.yaml