from rest_framework import serializers

from . models import Producr

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producr
        fields='__all__'
        """objec level validation"""
     
    def validate(self, data):
        if 'name' in data and len(data['name'])<2:
            raise serializers.ValidationError("Enter valide name")
        if 'condity'in data and data['condity'] <1:
            raise serializers.ValidationError("Enter a positive values")
        return data
