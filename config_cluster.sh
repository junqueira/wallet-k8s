
##config Kubernetes clusters


"/*     sample CRUD wallet    */"
kubectl create -f k8s/broker-deployment.yaml
kubectl create -f k8s/broker-service.yaml
kubectl create -f k8s/broker-ingress.yaml

kubectl get all
echo "your airflow available"
# minikube service nginx-svc --url
minikube service airflow-webserver --url