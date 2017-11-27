from django.db import models

class StringData(models.Model):
    data = models.CharField(max_length=30)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.id
