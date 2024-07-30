from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ServiceCategory, ServiceProvider, ServiceReview, UserProfile

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:  # Update 'meta' to 'Meta'
        model = ServiceCategory
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:  # Update 'meta' to 'Meta'
        model = ServiceProvider
        fields = '__all__'

class ServiceReviewSerializer(serializers.ModelSerializer):
    class Meta:  # Update 'meta' to 'Meta'
        model = ServiceReview
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
