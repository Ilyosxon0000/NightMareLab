from rest_framework import viewsets
from .serializers import *
from .models import *

class RequestTypeViewSet(viewsets.ModelViewSet):
    queryset = RequestType.objects.all()    
    serializer_class = RequestTypeSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()    
    serializer_class = RequestSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()    
    serializer_class = CompanySerializer
