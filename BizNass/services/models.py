from django.db import models
from django.contrib.auth.models import User

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