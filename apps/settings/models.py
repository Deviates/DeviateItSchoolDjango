from django.db import models

# Create your models here.
class Setting(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
        )
    descrtiptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True
        )
    email = models.CharField(
        max_length=255,
        verbose_name="Почта",
        blank=True,null=True

        )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    address_url = models.URLField(
        max_length=1000,
        verbose_name="Ссылка на адрес",
        blank = True, null = True
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True,null=True
    )
    youtube = models.URLField(
        verbose_name="Youtube",
        blank=True,null=True
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True
    )
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    first_image = models.ImageField(
        upload_to="about",
        verbose_name="Первая фотография"
        
    )
    second_image = models.ImageField(
        upload_to="about",
        verbose_name="Вторая фотография"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        
class AboutNumber(models.Model):
    teachers = models.CharField(
        max_length=255,
        verbose_name="Количество учителей"
    )
    students = models.TextField(
        verbose_name="Количество студентов"
    )
    company = models.TextField(
        verbose_name="Количество комании в которых работают"
    )
    alumni = models.TextField(
        verbose_name="Количество выпускников"
    )
    def __str__(self):
        return f"Учителей: {self.teachers} - Студентов: {self.students} - Компаний в которых работают: {self.company} - Выпускников: {self.alumni}"
    
    class Meta:
        verbose_name = "Мы в числах"
        verbose_name_plural = "Мы в числах"