from rest_framework import generics, permissions

from .serializers import ProductSerializer, LessonSerializer, CustomProductSerializer
from ..courses.models import Product, Lesson


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id, product__access__user=self.request.user)


class CustomProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CustomProductSerializer