from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer


class UserView(viewsets.ModelViewSet):
    """
    API endpoint for our users ;)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupView(viewsets.ModelViewSet):
    """
    API endpoint for groups ;)
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]