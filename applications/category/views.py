from applications.category.models import Category
from applications.category.serializers import CategorySerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS


class CategoryviewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()

