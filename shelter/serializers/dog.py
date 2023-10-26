
from rest_framework import serializers

from shelter.models import Dog, Breed
from shelter.serializers.breed import BreedDetailSerializer


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'


class DogDetailSerializer(serializers.ModelSerializer):
    #отдельный сериализатор чтобы в детальном представлении выводилось только имя и порода
    breed = BreedDetailSerializer() # так бы мы вывели всю инфу об этой породе
    # same_breed_dogs = serializers.IntegerField(source='filter()')
    same_breed_dogs = serializers.SerializerMethodField()

    def get_same_breed_dogs(self, instance):
        qty = Dog.objects.filter(breed=instance).count()
        return qty

    class Meta:
        model = Dog
        fields = ('name', 'breed', 'same_breed_dogs')
