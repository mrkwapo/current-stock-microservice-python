# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:28:24 2020

@author: Nate Kwapo
"""
# Current Stock Data Microservice
## Technologies used
* Python
* Flask
* py-eureka-client
* Spyder IDE
* Anaconda Prompt


## Steps to set up Development Environment

>Open Anaconda Prompt

>conda create --name <environment-name> python=3.7

>conda activate <environment-name>

>pip install flask

>create file in working directory: filename.py

>set Flask_APP=filename.py

>flask run 

# Configuration to register as a Eureka Client

import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 9090
### (The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds)
eureka_client.init_registry_client(eureka_server="http://localhost:8761/,http://localhost:8761/eureka",
                                app_name="this-name-will-show-on-eureka-page",
                                instance_port=5000)