from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="blog_image/",
        verbose_name="Фотография"
    )
    tags = models.CharField(
        max_length=255,
        verbose_name="Теги"
    )
    created_add = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Новости"
       