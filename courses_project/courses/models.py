from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    min_students = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()


    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name