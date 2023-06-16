from rest_framework import routers

from applications.category.views import CategoryviewSet


router = routers.DefaultRouter()
router.register('category', CategoryviewSet, 'category')

urlpatterns = router.urls