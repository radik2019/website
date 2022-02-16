from django.db import models
from django.urls import reverse


class Electronics(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True, )
    opsys = models.ForeignKey("OperatingSystem", on_delete=models.PROTECT, null=True)
    
    def get_absolute_url(self):
        return reverse("all_article", kwargs={"article_id": self.pk})
    
    def __str__(self):
        return self.title


class OperatingSystem(models.Model):
    name = models.CharField(max_length=40, db_index=True)


