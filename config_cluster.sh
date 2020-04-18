
##config Kubernetes clusters

kubectl create -f k8s/broker-deployment.yaml
kubectl create -f k8s/broker-service.yaml
kubectl create -f k8s/broker-ingress.yaml

kubectl get all

echo "your app dispose"
minikube service nginx-svc --url