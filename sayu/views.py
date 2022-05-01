from django.shortcuts import render
from rest_framework import viewsets
from .models import Users, Chats, Shared
from .serializers import UsersSerializer, ChatsSerializer, SharedSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all().order_by('id1')
    serializer_class = ChatsSerializer

class SharedViewSet(viewsets.ModelViewSet):
    queryset = Shared.objects.all().order_by('owner_id')
    serializer_class = SharedSerializer