
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shelter.models import Dog
from shelter.paginators import DogPaginator
from shelter.serializers.breed import DogListSerializer

from shelter.serializers.dog import DogDetailSerializer, DogSerializer
from shelter.tasks import SendSetLikeMessage
from users.models import User
from users.permissions import IsModerator, IsDogOwner, IsPublicDog


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]


class DogListAPIView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DogPaginator


class DogRetrieveAPIView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    # serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator | IsPublicDog]


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator]


class DogDeleteAPIView(DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]


class SetDogLike(APIView):
    def post(self, request):
        user = get_object_or_404(User, pk=request.data.get('user'))
        dog = get_object_or_404(Dog, pk=request.data.get('dog'))
        if dog.likes.filter(pk=user.pk).exists():
            return Response({"result": f'У {dog} уже есть лайк от {user}'}, status=200)
        dog.likes.add(user)
        SendSetLikeMessage.delay(user.username)
        return Response({"result": f'Лайк добавлен собаке {dog} от {user}'}, status=200)
