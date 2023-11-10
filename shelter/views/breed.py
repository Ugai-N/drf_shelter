from django.db.models import Count
from rest_framework import viewsets

from shelter.models import Breed
from shelter.serializers.breed import BreedListSerializer, BreedDetailSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    # serializer_class = BreedDetailSerializer
    queryset = Breed.objects.all()
    # related_name # аннотировали поле dog_count подсчетом всех объеков с related_name dog
    #  это будет работать только в BreedListSerializer, т.к с этом сериаоизаторе заведено поле
    default_serializer = BreedSerializer
    serializers_list = {
        'list': BreedListSerializer,
        'retrieve': BreedDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers_list.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs): # переопределяем метод list
        # self.queryset = Breed.objects.annotate(dog_count=Count('dog'))
        self.queryset = self.queryset.annotate(dog_count=Count('dog'))
        return super().list(request, *args, **kwargs)
