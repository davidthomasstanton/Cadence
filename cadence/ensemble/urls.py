from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EnsembleViewSet, SongViewSet, SetViewSet, ChartViewSet, TrackViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ensembles', EnsembleViewSet)
router.register(r'songs', SongViewSet)
router.register(r'sets', SetViewSet)
router.register(r'charts', ChartViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('index/', views.index, name='index'),
]