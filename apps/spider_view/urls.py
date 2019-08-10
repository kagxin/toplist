from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.spider_view.views import *

router = DefaultRouter()

router.register('entry', EntryViewSet, basename='entry')


urlpatterns = [
    path('', include(router.urls)),
    path('site-type/', SiteTypeView.as_view())
]