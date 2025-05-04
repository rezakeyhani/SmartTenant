from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, RentalContractViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'contracts', RentalContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]