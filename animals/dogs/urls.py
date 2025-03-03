from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dogs.views import DogViewSet, BreedViewSet


router = DefaultRouter()
router.register('dogs', DogViewSet)
router.register('breeds', BreedViewSet)

urlpatterns = [
    path('', include(router.urls))
]
