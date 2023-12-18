from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalData
        fields = '__all__'
        # exclude = ['id', 'title']

    def validate(self, attrs):
        return super().validate(attrs)