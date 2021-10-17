from django.db import models

# Create your models here.
class Cliente(models.Model):
    iddoc = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=120)
    municipio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    nombre_contacto = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon_social
        
    
