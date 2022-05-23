from django.db import models


class Entity(models.Model):
    """
    Entity DB schema
    """

    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField()
