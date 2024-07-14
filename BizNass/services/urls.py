from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewset, ServiceProviderViewset, ServiceReviewViewset

router = DefaultRouter()
router.register(r'categories',ServiceCategoryViewset )
router.register(r'providers',ServiceProviderViewset )
router.register(r'reviews',ServiceReviewViewset )

urlpatterns = [
    path('', include(router.urls)),
]
