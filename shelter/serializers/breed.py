from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField

from shelter.models import Breed, Dog


class DogListSerializer(serializers.ModelSerializer):
    # отдельный сериализатор чтобы в списке выводилось только имя и порода
    # breed = BreedSerializer() # так бы мы вывели всю инфу об этой породе
    breed = SlugRelatedField(slug_field='breed', queryset=Breed.objects.all())

    # так можно вытащить выводить название поля связанной сущности, а не номер ключа

    class Meta:
        model = Dog
        fields = ('name', 'breed', 'author')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class BreedListSerializer(serializers.ModelSerializer):
    dog_count = IntegerField()

    class Meta:
        model = Breed
        fields = ('breed', 'id', 'dog_count')


class BreedDetailSerializer(serializers.ModelSerializer):
    # dogs_of_breed = DogListSerializer() #- циклическая ссылка
    dogs_of_breed = serializers.SerializerMethodField()

    def get_dogs_of_breed(self, instance):
        # return [dog.name for dog in Dog.objects.filter(breed=instance)]
        return DogListSerializer(Dog.objects.filter(breed=instance), many=True).data

    class Meta:
        model = Breed
        fields = '__all__'

