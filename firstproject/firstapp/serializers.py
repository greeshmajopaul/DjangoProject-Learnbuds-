from rest_framework import serializers
from .models import Employee

class EmployeeSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','age','salary']