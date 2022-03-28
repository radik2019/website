from django.db import models
from django.urls import reverse


class Electronics(models.Model):
    title = models.CharField(max_length=254, verbose_name="Brand")
    content = models.TextField(unique=True, verbose_name="Modello")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creato")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Modificato")
    opsys = models.ForeignKey("OperatingSystem", on_delete=models.PROTECT, null=True)
    
    def get_absolute_url(self):
        return reverse("dettailed", kwargs={"article_id": self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Smartphone"
        ordering = ['time_create', 'title']


class OperatingSystem(models.Model):
    name = models.CharField(max_length=40, db_index=True, unique=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sistema operativo"
        verbose_name_plural = "Sistemi operativi"
        ordering = ['name']
        
        


