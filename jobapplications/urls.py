from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'applications', JobApplicationViewSet)
router.register(r'payments', PaymentViewSet, basename='payment')  # Register PaymentViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include both viewsets' routes
]
