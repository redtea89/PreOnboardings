from rest_framework import serializers

from .models import Advertiser, AdvertisingData


class AdvertiserCLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advertiser
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']
        

class AdvertiserRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advertiser
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']

