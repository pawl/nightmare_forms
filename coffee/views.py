# from .forms import MyForm
from coffee import models, serializers
from rest_framework import generics


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the currently active products.
        """
        return models.Product.objects.filter(is_active=True).order_by('name')
