from .models import Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'address1',
            'name_address1_unique',
            'address2',
            'point',
            'phone',
            'price_range',
            'parking',
            'opening_hours',
            'menu',
            'restaurant_type',
            'date_joined',
            'date_update',
        ]

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.title)
        instance.code = validated_data.get('address1', instance.code)
        instance.linenos = validated_data.get('name_address1_unique', instance.linenos)
        instance.language = validated_data.get('address2', instance.language)
        instance.style = validated_data.get('point', instance.style)
        instance.title = validated_data.get('phone', instance.title)
        instance.code = validated_data.get('price_range', instance.code)
        instance.linenos = validated_data.get('parking', instance.linenos)
        instance.language = validated_data.get('opening_hours', instance.language)
        instance.style = validated_data.get('menu', instance.style)
        instance.style = validated_data.get('restaurant_type', instance.style)
        instance.style = validated_data.get('date_joined', instance.style)
        instance.style = validated_data.get('date_update', instance.style)
        instance.save()
        return instance
