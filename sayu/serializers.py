from rest_framework import serializers
from .models import Users, Chats, Shared

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'login', 'password', 'seed', 'token', 'email', 'social', 'location', 'birthday', 'hobby', 'career', 'education', 'cigaretes', 'alcohol', 'music', 'films', 'videogames', 'serials', 'books')

class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ("id1", "id2", "location")

class SharedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shared
        fields = ('owner_id', 'shared_id', 'field')