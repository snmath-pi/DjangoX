from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude=['father_name', ]
        fields = '__all__'

    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError('Age cannot be less than 18')
        for x in data['name']:
            if x >='0' and x<='9':
                raise serializers.ValidationError('Name must contain alphabets only')
        
        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model=Book
        fields='__all__'