from rest_framework import serializers
from . import models 

class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestType
        fields = "__all__"

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"