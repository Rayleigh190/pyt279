from django.db import models


class Breakfast(models.Model):
    group = models.IntegerField()
    name = models.CharField(max_length=5)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name
# Create your models here.
