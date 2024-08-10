from django.db import models
from django.contrib.auth.models import User
import stripe
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #ForignKey
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class ServiceReview(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='reviews') #Forign Key ?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.service_provider.name}' 
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username}"

    def charge(self, token):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=int(self.amount * 100),  # Stripe uses cents, hence multiplying by 100
            currency='usd',
            description=f"Charge for {self.user.email}",
            source=token,
        )
        self.stripe_charge_id = charge['id']
        self.save()