from rest_framework import serializers
from . import models


class WishListSerializers(serializers.ModelSerializer):
    id=serializers.ReadOnlyField(source='product.id')
    title=serializers.ReadOnlyField(source='product.title')
    description=serializers.ReadOnlyField(source='product.description')
    is_Featured=serializers.ReadOnlyField(source='product.is_Featured')
    clothesType=serializers.ReadOnlyField(source='product.clothesType')
    ratings=serializers.ReadOnlyField(source='product.ratings')
    category=serializers.ReadOnlyField(source='product.category.id')
    brand=serializers.ReadOnlyField(source='product.brand.id')
    price=serializers.ReadOnlyField(source='product.price')
    colors=serializers.ReadOnlyField(source='product.colors')
    sizes=serializers.ReadOnlyField(source='product.sizes')
    imageUrls=serializers.ReadOnlyField(source='product.imageUrls')
    created_at=serializers.ReadOnlyField(source='product.created_at')
    
    class Meta:
        model=models.Wishlist
        fields=['id','title','description','price','is_Featured','clothesType','ratings','category','colors','sizes','imageUrls','created_at','brand']