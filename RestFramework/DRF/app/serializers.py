from rest_framework import serializers , permissions
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_marks(self , value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Marks must be between 0 and 100.")
        return value
    
    def get_permissions(self):
        return [permissions.isAuthenticated()]