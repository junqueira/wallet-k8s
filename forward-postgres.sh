
# opa, pod postgres tem acesso brindado, e ele ficar disponivel com acesso 
# externo ao cluster tem que fazer um port forward 

kubectl port-forward \
$(kubectl get pods --all-namespaces|grep postgres|awk '{print $2}') \
5432:5432

# kubectl proxy --port=8080