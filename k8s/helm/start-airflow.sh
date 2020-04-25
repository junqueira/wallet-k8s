


helm repo add kedacore https://kedacore.github.io/charts
helm repo add astronomer https://helm.astronomer.io

helm repo update

kubectl create namespace keda
helm install keda \
    --namespace keda kedacore/keda

kubectl create namespace airflow

helm install airflow \
    --set executor=CeleryExecutor \
    --set workers.keda.enabled=true \
    --set workers.persistence.enabled=false \
    --namespace airflow \
    astronomer/airflow


kubectl port-forward service/airflow-webserver 8080:8080 -n airflow