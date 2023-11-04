from rest_framework import serializers
from . import models

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserType
        fields = "__all__"