from rest_framework import serializers
from .models import ServiceCategory, ServiceProvider, ServiceReview


class ServiceCategorySerializer(serializers.ModelSerializer):
    class meta :
        model = ServiceCategory
        fields = '__all__'
class ServiceProviderSerializer(serializers.ModelSerializer):
    class meta :
        model = ServiceProvider
        fields = '__all__'

class ServiceReviewSerializer(serializers.ModelSerializer):
    class meta :
        model = ServiceReview
        fields = '__all__'