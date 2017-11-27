from .models import StringData
from rest_framework import serializers

class StringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringData
        fields = ('id', 'data', 'value')
