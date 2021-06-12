from django.db import models

# Create your models here.
class Parroquia(models.Model):
    class Meta:
        verbose_name_plural = "Parroquias"

    tipos_parroquia = (('Urbana', 'Urbana'),('Rural', 'Rural'))
    nombre = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30, choices=tipos_parroquia  ) 

    def __str__(self):
        return "%s - %s" % (self.nombre, self.tipo)
        
class BarrioCiudadela(models.Model):
    class Meta:
        verbose_name_plural = "Barrios o ciudadelas"
    
    nombre = models.CharField(max_length=30)
    numero_viviendas = models.IntegerField("Cantidad de viviendas") 
    numero_parques = models.IntegerField("Cantidad de parques") 
    numero_edificios = models.IntegerField("Cantidad de edificios")
    
    id_parroquia = models.ForeignKey("Parroquia", related_name='barrios',  on_delete=models.CASCADE) 

    def __str__(self):
        return "Nombre: %s - Viviendas: %s - Parques: %s - Edificios: %s" % (
            self.nombre, 
            self.numero_viviendas, 
            self.numero_parques, 
            self.numero_edificios)