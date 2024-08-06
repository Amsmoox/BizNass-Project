from rest_framework import viewsets, generics
from .models import ServiceCategory, ServiceProvider, ServiceReview
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceReviewSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

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


def index(request):
    return render(request, 'services/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'services/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'services/login.html')

def profile(request):
    return render(request, 'services/profile.html')
