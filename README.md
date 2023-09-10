## Django RabbitMQ Microservices
This is a django project that has 3 micro serivces all communicationg together with RabbitMq. This project is inspired by https://github.com/mansha99/django-rabbitmq-microservice and a detailed blog https://medium.com/@mansha99/microservices-in-python-django-rabbitmq-and-pika-fe1adb0c6a1a


## Project setup
```
pip3 install requirements.txt
```

## Start rabbitMq from docker
```
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

## Start the 3 applications in their folders
```
python3 manage.py runserver
```

