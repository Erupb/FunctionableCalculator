from django.contrib.auth.models import User
from django.db import models


class History(models.Model):
    operation_type = models.CharField(max_length=55)
    creation_time = models.CharField(max_length=35)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    result = models.CharField(max_length=55)
    equation = models.CharField(max_length=30, default='')


class ElementaryMath(models.Model):
    result = models.CharField(max_length=50)


class Equation(models.Model):
    result = models.CharField(max_length=50)


class Antiderivative(models.Model):
    result = models.CharField(max_length=50)
