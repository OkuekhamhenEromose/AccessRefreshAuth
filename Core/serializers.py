
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'first_name', 'last_name', 'email']#this could be used when you want to return the user object when the user logs in

