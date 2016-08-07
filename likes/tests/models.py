from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=10)
