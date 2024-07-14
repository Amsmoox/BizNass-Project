from django.shortcuts import render
from rest_framework import viewsets
from .models import ServiceCategory, ServiceProvider, ServiceReview
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceReviewSerializer

# Create your views here.

class ServiceCategoryViewset(viewsets.ModelViewSet):
    queryset = ServiceCategory.object.all()
    serializer_class = ServiceCategorySerializer

class ServiceProviderViewset(viewsets.ModelViewSet):
    queryset = ServiceProvider.object.all()
    serializer_class = ServiceProviderSerializer

class ServiceReviewViewset(viewsets.ModelViewSet):
    queryset = ServiceReview.object.all()
    serializer_class = ServiceReviewSerializer