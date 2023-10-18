from emr.patients.models import Patient
from rest_framework.views import APIView
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        return patient