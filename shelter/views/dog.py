from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from shelter.models import Dog
from shelter.serializers.dog import DogSerializer


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer


class DogListAPIView(ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogRetrieveAPIView(RetrieveAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()
