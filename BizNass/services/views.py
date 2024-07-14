from django.shortcuts import render
from rest_framework import viewsets
from .models import ServiceCategory, ServiceProvider, ServiceReview
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceReviewSerializer

# Create your views here.

class ServiceCategoryViewset(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceProviderViewset(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

class ServiceReviewViewset(viewsets.ModelViewSet):
    queryset = ServiceReview.objects.all()
    serializer_class = ServiceReviewSerializer