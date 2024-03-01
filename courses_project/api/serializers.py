from django.contrib.auth.models import User
from django.db.models import Max
from rest_framework import serializers

from courses_project.courses.models import Lesson, Product, ProductAccess, Group


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    # Возвращает количество уроков
    def get_lesson_count(self, product):
        return Lesson.objects.filter(product=product).count()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'cost', 'min_students', 'max_students', 'lesson_count']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'product']


class CustomProductSerializer(serializers.ModelSerializer):
    student_count = serializers.SerializerMethodField()
    group_fill_percentage = serializers.SerializerMethodField()
    product_acquisition_percentage = serializers.SerializerMethodField()

    # Возвращает количество учеников
    def get_student_count(self, product):
        return ProductAccess.objects.filter(product=product).count()

    # Возвращает процент заполненных групп
    def get_group_fill_percentage(self, product):
        max_group_size = Group.objects.filter(product=product).aggregate(max_size=Max('students__count'))['max_size']
        if max_group_size:
            total_students = self.get_student_count(product)
            total_groups = Group.objects.filter(product=product).count()
            average_group_size = total_students / total_groups
            fill_percentage = (average_group_size / max_group_size) * 100
            return fill_percentage
        else:
            return 0

    # Возвращает процент приобретенных продуктов
    def get_product_acquisition_percentage(self, product):
        total_users = User.objects.count()
        access_count = ProductAccess.objects.filter(product=product).count()
        if total_users > 0:
            acquisition_percentage = (access_count / total_users) * 100
            return acquisition_percentage
        else:
            return 0

    class Meta:
        model = Product
        fields = ['id', 'name', 'student_count', 'group_fill_percentage', 'product_acquisition_percentage', 'start_date', 'cost', 'min_students', 'max_students']