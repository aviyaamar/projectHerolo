from django.shortcuts import render
from rest_framework import viewsets
from .models import Messages
from django.contrib.auth import get_user_model
from .serializer import UserSerializer, MessageSerializer
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

class UserMessagesViewSet(viewsets.ViewSet):
    """
    A simple viewSet for listing users Messages
    """

    def list(self, request):
        user = get_user_model().objects.get(pk=request.user.id)
        print(user)
        queryset = Messages.objects.filter(Q(sender=user) | Q(recevier =user))
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer