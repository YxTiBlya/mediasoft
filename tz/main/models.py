from django.db import models

class City(models.Model):
    cityName = models.CharField('Название города', max_length=20)
    cityStreet = models.TextField('Улицы')

    def __str__(self):
        return self.cityName

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Shop(models.Model):
    shopName = models.CharField('Название магазина', max_length=20)
    shopCity = models.CharField('Город', max_length=20)
    shopStreet = models.CharField('Улица', max_length=25)
    shopHouse = models.IntegerField('Дом')
    shopTO = models.TimeField('Время открытия')
    shopTC = models.TimeField('Время закрытия')

    def __str__(self):
        return self.shopName

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'