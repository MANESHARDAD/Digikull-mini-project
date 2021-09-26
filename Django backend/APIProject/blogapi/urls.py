from django.urls import path
from django.urls.conf import include
from .views import ArticleViewset, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewset, basename='articles')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
   
]
