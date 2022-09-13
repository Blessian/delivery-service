from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """

        """
        if self.action == 'retrieve' or 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
