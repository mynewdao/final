from django.db import models

from category.models import Category

class ShopItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.CharField('Бренд', max_length=16)
    model = models.CharField('Модель', max_length=32)
    condition = models.CharField('Состояние', max_length=20)
    quantity = models.IntegerField('Колличество')
    color = models.TextField('Цвет')
    info = models.TextField('Характеристики')
    price = models.IntegerField('Цена')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    image5 = models.ImageField(upload_to='images/')
