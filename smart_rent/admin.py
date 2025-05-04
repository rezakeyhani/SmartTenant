from django.contrib import admin
from .models import Tenant,Property,RentalContract

admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(RentalContract)

