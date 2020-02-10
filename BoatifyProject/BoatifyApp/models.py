from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    @classmethod
    def get(self):
        return self.email