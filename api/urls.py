from rest_framework.routers import DefaultRouter

from api.views import BlogsView

urlpatterns = []

router = DefaultRouter()
router.register(r'api/blogs', BlogsView)


urlpatterns += router.urls