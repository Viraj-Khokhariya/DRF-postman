from rest_framework import serializers
from .models import Student 

# Create your models here.
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fname = serializers.CharField(max_length=50)
    lname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    contact = serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)