from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
  # name = serializers.CharField(max_length=200)
  # email = serializers.EmailField()
  # reg_no = serializers.CharField()

  class Meta:
    model = Student
    # fields = ('id', 'name', 'email', 'reg_no')
    fields = "__all__"

  # def create(self, validated_data):
  #   return Student.objects.create(**validated_data)