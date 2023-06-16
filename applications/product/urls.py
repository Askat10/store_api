from rest_framework import routers

from applications.product.views import ProductViewSet


router = routers.DefaultRouter()

router.register('product', ProductViewSet, 'products')

urlpatterns = router.urls
