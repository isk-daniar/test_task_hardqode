from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """ Продукт """

    author = models.ForeignKey('Автор продукта', User, on_delete=models.CASCADE)

    name = models.CharField('Название продукта',max_length=100)
    start_date = models.DateTimeField('Дата и время старта продукта')
    cost = models.DecimalField('Cтоимость продукта', max_digits=8, decimal_places=2)

    min_students = models.PositiveIntegerField('Минимальное количество юзеров')
    max_students = models.PositiveIntegerField('Максимальное количество юзеров')


    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    """ Доступ к продукту """

    product = models.ForeignKey('Продукт', Product, on_delete=models.CASCADE)
    users = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE)


class Lesson(models.Model):
    """ Урок """

    product = models.ForeignKey('Продукт, к которому принадлежит урок', Product, on_delete=models.CASCADE)
    name = models.CharField('Название урока', max_length=100)
    video_link = models.CharField('Ссылка на видео урока', max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    """ Группа """

    product = models.ForeignKey('Продукт, к которому принадлежит группа',Product, on_delete=models.CASCADE)
    name = models.CharField('Название группы', max_length=100)
    students = models.ManyToManyField('Ученики, состоящие в группе', User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name