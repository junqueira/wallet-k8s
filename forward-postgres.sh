
kubectl port-forward \
$(kubectl get pods --all-namespaces|grep postgres|awk '{print $2}') \
5432:5432

# kubectl proxy --port=8080