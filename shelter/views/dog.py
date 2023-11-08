from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from shelter.models import Dog
from shelter.serializers.breed import DogListSerializer

from shelter.serializers.dog import DogDetailSerializer, DogSerializer
from users.permissions import IsModerator, IsDogOwner, IsPublicDog


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]


class DogListAPIView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]


class DogRetrieveAPIView(RetrieveAPIView):
    # serializer_class = DogDetailSerializer
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator | IsPublicDog]


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator]


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]
