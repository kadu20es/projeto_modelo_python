# Representação dos dados no banco de dados

from django.db import models

class Users(models.Model):
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name