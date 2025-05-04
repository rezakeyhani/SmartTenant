from django.db import models

class Tenant(models.Model):
    full_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class RentalContract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='contracts')
    property_address = models.CharField(max_length=300)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    contract_pdf = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f'Contract with {self.tenant.full_name} ({self.property_address})'