from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', include('services.urls')),
    path('', include('services.urls')),  
    path('', include('BizNass.auth_urls')),  # Include the new auth URLs
]
