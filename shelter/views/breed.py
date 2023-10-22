from rest_framework import viewsets

from shelter.models import Breed
from shelter.serializers.breed import BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
