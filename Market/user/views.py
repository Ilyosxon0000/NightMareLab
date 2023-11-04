from rest_framework import viewsets
from .serializers import *
from .models import *

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
