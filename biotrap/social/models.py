from django.db import models


# Create your models here.
class Link(models.Model):
    key = models.SlugField("nombre clave", max_length=100, unique=True)
    name = models.CharField("red social", max_length=200)
    url = models.URLField("enlace", max_length=200, blank=True)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificación", auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name
