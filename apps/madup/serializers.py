from rest_framework import serializers

from .models import Advertiser, AdvertisingData


class AdvertiserCLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advertiser
        fields = '__all__'
        read_only_fields = []
        # extra_kwargs = {
        #     'sample_field': {'write_only': True},
        # }
        

class AdvertiserRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advertiser
        fields = '__all__'


class AnalysisViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AdvertisingData
        fields = '__all__'
        read_only_fields = []
        # extra_kwargs = {
        #     'sample_field': {'write_only': True},
        # }