# airflow
## 1. Build the docker image : 
```bash
docker build --pull --rm -f 'dockerfile' -t 'airflow_demo:latest' '.'
```

## 2. Start standalone airflow: 
```bash
docker compose -f 'docker_compose.yml' up -d --build
```

## 3. Install required python package to author DAG
```bash
pip install apache-airflow
```
## Copy DAGs
Copy dags folder in auto-generated airflow folder. Run dag file to see it on UI

## webserver UI:
```bash
http://localhost:8080/
user- admin
password - is in airflow/standalone_admin_password.txt
```
