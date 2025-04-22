# airflow
Build the docker image : 
docker build --pull --rm -f 'dockerfile' -t 'airflow_demo:latest' '.'

Start standalone airflow: 
docker compose -f 'docker_compose.yml' up -d --build  

Install required python package to author DAG
pip install apache-airflow

Copy dags folder in auto-generated airflow folder 
run dag file to see it on UI

webserver UI:
http://localhost:8080/
user- admin
password - is in airflow/standalone_admin_password.txt