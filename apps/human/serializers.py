from rest_framework import serializers

from .models import Research


class ResearchCLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Research
        fields = '__all__'


class ResearchRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Research
        fields = '__all__'