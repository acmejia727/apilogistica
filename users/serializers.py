from rest_framework import serializers
from users.models import CustomsUser as User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'