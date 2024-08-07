from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class TaskResult(models.Model):
    task_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
