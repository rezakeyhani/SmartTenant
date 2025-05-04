from django.shortcuts import render

from rest_framework import viewsets
from .models import Tenant, RentalContract
from .serializers import TenantSerializer, RentalContractSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class RentalContractViewSet(viewsets.ModelViewSet):
    queryset = RentalContract.objects.all()
    serializer_class = RentalContractSerializer