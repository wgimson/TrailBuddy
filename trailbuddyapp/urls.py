from rest_framework import routers
from .api import LocationViewset

router = routers.DefaultRouter()
router.register('api/locations', LocationViewset, 'locations')

urlpatterns = router.urls