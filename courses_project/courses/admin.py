from django.contrib import admin

from courses_project.courses.models import Product, ProductAccess, Lesson, Group

admin.site.register(Product)
admin.site.register(ProductAccess)
admin.site.register(Lesson)
admin.site.register(Group)

