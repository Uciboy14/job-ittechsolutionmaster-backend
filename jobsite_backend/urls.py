# jobsite_backend/urls.py
from django.contrib import admin
from django.urls import path, include  # Include is necessary for adding app URLs
from rest_framework import routers
from jobapplications.views import JobApplicationViewSet  # Replace 'your_app_name' with the actual name of your app

# Create a router and register our viewset with it
router = routers.DefaultRouter()
router.register(r'applications', JobApplicationViewSet)  # Register the viewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the API URLs under the 'api/' path
]
