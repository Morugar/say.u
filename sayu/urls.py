from django.db import router
from django.urls import include, path
from rest_framework import routers
from . import views

routerUsers = routers.DefaultRouter()
routerUsers.register(r'Users', views.UserViewSet)
routerChats = routers.DefaultRouter()
routerChats.register(r'Chats', views.ChatViewSet)
routerShared = routers.DefaultRouter()
routerShared.register(r'Shared', views.SharedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(routerUsers.urls)),
    path('', include(routerChats.urls)),
    path('', include(routerShared.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]