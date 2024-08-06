from rest_framework import viewsets, generics
from .models import ServiceCategory, ServiceProvider, ServiceReview
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceReviewSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny

class ServiceCategoryViewset(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceProviderViewset(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

class ServiceReviewViewset(viewsets.ModelViewSet):
    queryset = ServiceReview.objects.all()
    serializer_class = ServiceReviewSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
