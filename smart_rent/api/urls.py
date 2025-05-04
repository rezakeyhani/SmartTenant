

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, PropertyViewSet, RentalContractViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'contracts', RentalContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]