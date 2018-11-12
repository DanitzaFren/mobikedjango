from django.db import models

# Create your models here.


from django.utils import timezone


class Cliente(models.Model):
    rut =models.CharField(max_length=12)
    nombre = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    nrotarjeta= models.CharField(max_length=200)
    contraseña=models.CharField(max_length=200)



 