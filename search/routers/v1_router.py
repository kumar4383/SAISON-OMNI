from rest_framework.routers import DefaultRouter

from search.views.v1 import ESViewSet

prefix = "v1"
router = DefaultRouter()

router.register(f"{prefix}", ESViewSet, basename="elastic_search")

urlpatterns = []