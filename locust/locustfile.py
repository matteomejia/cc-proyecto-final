import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def workshops(self):
        self.client.get("/workshops/")

    @task
    def home(self):
        self.client.get("/")