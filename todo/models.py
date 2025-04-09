from django.db import models
class Tarea(models.Model):
    tarea=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    def __str__(self):
        return self.tarea


