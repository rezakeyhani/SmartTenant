
from rest_framework import serializers
from smart_rent.models import Tenant, Property, RentalContract

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class RentalContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalContract
        fields = '__all__'