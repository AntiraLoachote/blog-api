#customers/urls.py

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from myblog.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, base_name='post')

urlpatterns = [
    url(r'', include(router.urls)),
]
