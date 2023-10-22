from django.urls import path
from rest_framework.routers import DefaultRouter

from shelter.apps import ShelterConfig
from shelter.views.breed import BreedViewSet
from shelter.views.dog import DogCreateAPIView, DogListAPIView, DogRetrieveAPIView, DogUpdateAPIView, DogDeleteAPIView

app_name = ShelterConfig.name

router = DefaultRouter()
router.register(r'breed', BreedViewSet, basename='breeds')

urlpatterns = [
                  path('create/', DogCreateAPIView.as_view(), name='create_dog'),
                  path('', DogListAPIView.as_view(), name='dog_list'),
                  path('<int:pk>/', DogRetrieveAPIView.as_view(), name='view_dog'),
                  path('<int:pk>/edit/', DogUpdateAPIView.as_view(), name='edit_dog'),
                  path('<int:pk>/delete/', DogDeleteAPIView.as_view(), name='delete_dog'),
              ] + router.urls
