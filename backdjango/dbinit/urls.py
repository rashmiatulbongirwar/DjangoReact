from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('dbinit', views.UserInfoViewSet)
router.register('org member', views.OrgMemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
