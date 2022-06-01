from rest_framework import serializers

from .models import Group, Restaurant, Pos


class GroupCLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'
        

class GroupRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class RestaurantCLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = '__all__'
        

class RestaurantRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = '__all__'
