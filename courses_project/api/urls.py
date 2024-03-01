from django.urls import path

from courses_project.api.views import ProductListAPIView, LessonListAPIView, CustomProductListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('custom_products/', CustomProductListAPIView.as_view(), name='custom-product-list'),
]
