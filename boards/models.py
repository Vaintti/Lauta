from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=10)

    def __str__(self):
        return self.name
