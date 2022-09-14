from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    User CRUD
    비밀번호가 일치하면 update 가능
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        user_instance = self.get_object()
        user = User.objects.get(id=user_instance.id)
        serializer = self.get_serializer(user_instance, data=request.data)
        if serializer.is_valid(raise_exception=True) and user.check_password(request.data['password']):
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        """
        사용자 권한 부여
        """
        if self.action is 'update' and 'partial_update' and 'destroy':
            permission_classes = [IsAuthenticated]
        elif self.action is 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
