from django.db import models

from django.contrib.auth.models import User 


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    vencimiento = models.DateField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)

  
    
    def __str__(self):
        
        return self.nombre