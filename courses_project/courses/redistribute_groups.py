from django.contrib.auth.models import User
from rest_framework.response import Response

from courses_project.courses.models import Group, Product, ProductAccess


def redistribute_groups(product, user_id, product_id):
    # Получение информации о пользователе и продукте
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)

    # Проверка, есть ли у пользователя доступ к продукту
    if ProductAccess.objects.filter(user=user, product=product).exists():
        return Response("Пользователь имеет доступ к продукту")

    # Получение групп, принадлежащих продукту
    groups = Group.objects.filter(product=product)

    # Проверка, есть ли свободные места в существующих группах
    for group in groups:
        if group.students.count() < product.max_students:
            # Добавление пользователя в группу
            group.students.add(user)
            return Response("Пользователь успешно добавлен в группу")
        else:
            return Response("Пользователь уже добавлен")