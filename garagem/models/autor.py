from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name_plural = "Autores"