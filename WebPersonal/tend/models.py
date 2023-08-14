from django.db import models

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tendencia"
        verbose_name_plural = "Tendencias"
        ordering = ["-created"]



    def __str__(self):
        return self.title