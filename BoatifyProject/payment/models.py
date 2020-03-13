from django.db import models

# Create your models here.


class Seatres(models.Model):
    boatid = models.IntegerField()
    email = models.EmailField()
    seatid = models.CharField(max_length=50)


    def __str__(self):
        return str(self.boatid)