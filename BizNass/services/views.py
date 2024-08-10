from rest_framework import viewsets, generics
from .models import ServiceCategory, ServiceProvider, ServiceReview, Payment
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceReviewSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, PaymentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

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



@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment(
                user=request.user,
                amount=form.cleaned_data['amount']
            )
            payment.charge(form.cleaned_data['stripe_token'])
            return redirect('profile')
    else:
        form = PaymentForm()

    return render(request, 'services/payment.html', {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })