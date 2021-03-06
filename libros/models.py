
from django.db import models
from django.contrib import admin

class Libro (models.Model):
    nombre    = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    precio    = models.DecimalField(max_digits=5, decimal_places=2)
    unidades  = models.IntegerField()

    def __str__(self):
        return self.nombre

class Autor (models.Model):
    nombre  =   models.CharField(max_length=50)
    apellido =  models.CharField(max_length=50)
    genero =  models.CharField(max_length=50)
    libros = models.ManyToManyField(Libro, through='Clasificacion')

    def __str__(self):
        return self.nombre

class Clasificacion(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    extra = 1

class ClasificacionInLine(admin.TabularInline):
    model = Clasificacion
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    inlines = (ClasificacionInLine,)

class LibroAdmin (admin.ModelAdmin):
    inlines = (ClasificacionInLine,)
