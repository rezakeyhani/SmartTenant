from rest_framework import serializers
from .models import Tenant, RentalContract

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class RentalContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalContract
        fields = '__all__'