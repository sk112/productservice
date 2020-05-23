from rest_framework import serializers
from .models import *


class CategorySerialier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = quantity
        # fields = ('case_size_in_ml',
        #           'case_sale_rate',
        #           'bottle_mrp_rate',
        #           'bottle_in_case')

        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    # pk = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = CategorySerialier(many=True, read_only=True)
    quantity = QuantitySerializer(many=True, read_only=True)

    class Meta:
        model = ProductItem
        fields = ('item_id', 'item_desc', 'quantity', 'category')


# class ProductList(serializers.ModelSerializer):
#     product = Products(many=True, read_only=True)
#     quantity = Quantity(many=True, read_only=True)
#
#     class Meta:
#         model = ProductItem
#         fields = ['item_code', 'quantity']


# class ProductList(serializers.ListSerializer):
#     class Meta:
#         list_serializer_class = Products
