from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'  # This will include all the fields in the model
