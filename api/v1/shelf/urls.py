from rest_framework import routers

from api.v1.shelf.endpoints import ShelfViewSet

router = routers.SimpleRouter()
router.register(r"", ShelfViewSet, basename="shelf")

urlpatterns = router.urls
