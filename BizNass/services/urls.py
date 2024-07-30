from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewset, ServiceProviderViewset, ServiceReviewViewset, RegisterView

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewset)
router.register(r'providers', ServiceProviderViewset)
router.register(r'reviews', ServiceReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
