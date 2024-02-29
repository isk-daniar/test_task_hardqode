from rest_framework.response import Response

from courses_project.courses.models import Group, User, Product, ProductAccess


def redistribute_groups(product, user_id, product_id):
    # Получение информации о пользователе и продукте
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)

    # Проверка, есть ли у пользователя доступ к продукту
    if ProductAccess.objects.filter(user=user, product=product).exists():
        return Response("Пользователь уже имеет доступ к продукту.")

    # Получение групп, принадлежащих продукту
    groups = Group.objects.filter(product=product)

    # Проверка, есть ли свободные места в существующих группах
    for group in groups:
        if group.students.count() < product.max_students:
            # Добавление пользователя в группу
            group.students.add(user)
            return Response("Пользователь успешно добавлен в группу.")

    # Если все группы заполнены, создаем новую группу и добавляем пользователя в нее
    new_group = Group.objects.create(product=product, name="Group 1")  # Создание новой группы
    new_group.students.add(user)  # Добавление пользователя в новую группу
    return Response("Пользователь успешно добавлен в новую группу.")