from django.db import models

class Tenant(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class RentalContract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    contract_pdf = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.tenant.full_name} - {self.property.title}"