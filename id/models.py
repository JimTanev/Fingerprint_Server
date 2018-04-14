from django.db import models


class Person(models.Model):
    iden_num = models.CharField(max_length=10)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

