from rest_framework import routers

from sistemafundaj.noticias.views import NoticiasViewSet

router = routers.DefaultRouter()
router.register(r'noticias', NoticiasViewSet)

urlpatterns = router.urls