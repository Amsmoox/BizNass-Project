from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewset, ServiceProviderViewset, ServiceReviewViewset, index, register, user_login, profile

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewset)
router.register(r'providers', ServiceProviderViewset)
router.register(r'reviews', ServiceReviewViewset)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('api/', include(router.urls)),
]
