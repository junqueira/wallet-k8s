
## run Apache Airflow on Kubernetes clusters to app with sample CRUD wallet
    minikube
    django
    postgres

## test Airflow
    curl $(minikube service nginx-svc --url)/health
    [ "$1" = "webserver" ] || [ "$1" = "worker" ] || [ "$1" = "scheduler" ]

## Usage
![alt text](https://raw.githubusercontent.com/junqueira/wallet-k8s/master/app/wallet-k8s.png)


### load minikube
<pre>
    <code>
        ./start_minikube.sh
    </code>
</pre>

### config Kubernetes clusters
<pre>
    <code>
        ./config_cluster.sh
    </code>
</pre>


### GET `/<url>/wallet`:
<pre><code>
    curl http://3.94.130.173:8080/www.broker.com/wallet/
</code></pre>

### DELETE /:
Remove todos os dados da base.
<pre><code>
    curl -X "DELETE" http://3.94.130.173:8080/
</code></pre>