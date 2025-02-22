from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Color(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"



class Car(models.Model):
   category = models.ForeignKey(Category, on_delete=models.PROTECT)
   title = models.CharField(max_length=100)
   description = models.TextField()
   model = models.CharField(max_length=100)
   year = models.PositiveSmallIntegerField()
   engine_capacity = models.DecimalField(max_digits=3, decimal_places=1)
   odometer = models.PositiveSmallIntegerField()
   color = models.ForeignKey(Color, on_delete=models.PROTECT)
   image = models.ImageField(upload_to='media/car_images')


   def __str__(self):
       return f'{self.title} | {self.id}'

   class Meta:
       verbose_name = "Машина"
       verbose_name_plural = "Машины"

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



