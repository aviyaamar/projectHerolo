from rest_framework import serializers
from .models import Messages
from django.contrib.auth import get_user_model


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'sender', 'receiver', 'subject', 'message', 'creation_date')
        model = Messages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()