from django.db import models

class Shop(models.Model):
    title = models.CharField("Название", max_length=300)
    description = models.CharField("Описание", max_length=1000)
    imageUrl = models.URLField("Ссылка на изображение")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Магазин"
        verbose_name = "Магазины"