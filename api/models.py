from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  reg_no = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
