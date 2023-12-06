from rest_framework.routers import DefaultRouter
from apps.api.views import UsersModelViewset, BlogModelViewset

router: DefaultRouter = DefaultRouter()

router.register(r'users', UsersModelViewset)
router.register(r'posts', BlogModelViewset)