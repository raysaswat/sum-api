# sum-api with Dockerization

*********Please see the shared screenshot named as "mustsee" ***********************

1. This project contains a simple HTTP end point creation which will do a simple sum of two numbers.
2. For better handling of the code and enhancement, exception handling and modularity(function based implementaion) is provided.

3.The whole application is dockerized(Refer to Dockerfile inside mysite folder and docker image is created in the dockerhub).

Steps to run the application without Docker :
 1. Activate the virtual env(sum_venv) : source sum_venv/bin/activate
 2. pip install -r requirements.txt
 3. python manage.py runserver
 4. Open localhost:8000
 
 Steps to run the application with Docker :
 
 1.Pull the image from docker hub :
    docker image pull <yourdockerusername>/sum-docker
 2.Run the docker
    docker run -p 8888:5000 <yourdockerusername>/sum-docker
  
  
  https://docker-curriculum.com/ - For any information about containerization of Django web app


