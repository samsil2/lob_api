from django.db import models

# Create your models here.

class Address(models.Model):
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=5)
    zip = models.IntegerField()

    def __str__(self):
        return self.line1