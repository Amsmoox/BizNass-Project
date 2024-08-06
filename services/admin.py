from django.contrib import admin
from .models import ServiceCategory, ServiceProvider, ServiceReview
# Register your models here.


admin.site.register(ServiceCategory)
admin.site.register(ServiceProvider)
admin.site.register(ServiceReview)