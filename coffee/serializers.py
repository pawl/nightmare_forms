from coffee import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        depth = 3
