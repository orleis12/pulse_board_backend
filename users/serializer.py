from rest_framework import serializers
from .models import User, LandingPage, UserActivity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = '__all__'

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
