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

class Slide(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image= models.ImageField(
        upload_to="image_slide/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        
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
    students = models.CharField(
        max_length=255,
        verbose_name="Количество студентов"
    )
    company = models.CharField(
        max_length=255,
        verbose_name="Количество комании в которых работают"
    )
    alumni = models.CharField(
        max_length=255,
        verbose_name="Количество выпускников"
    )
    def __str__(self):
        return f"Учителей: {self.teachers} - Студентов: {self.students} - Компаний в которых работают: {self.company} - Выпускников: {self.alumni}"
    
    class Meta:
        verbose_name = "Мы в числах"
        verbose_name_plural = "Мы в числах"

class Team(models.Model):
    image = models.ImageField(
        upload_to="team_image/",
        verbose_name="Фотография"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    name = models.CharField(
        max_length=244,
        verbose_name="ФИО"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Работа"
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True,null=True
    )
    github = models.URLField(
        verbose_name="GitHub",
        blank=True,null=True
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"

class Gallery(models.Model):
    image =models.ImageField(
        upload_to="gallery_image/",
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    message = models.TextField(
        max_length=255,
        verbose_name="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"