from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from applications.product.serializers import ProductSerializer
from applications.product.models import Product
from permissions.permissions import IsOwnerOrIsAdminUser


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all() # TODO: optimize
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]

        return super().get_permissions()