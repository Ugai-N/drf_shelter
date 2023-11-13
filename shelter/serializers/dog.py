
from rest_framework import serializers

from shelter.models import Dog, Breed
from shelter.serializers.breed import BreedDetailSerializer, BreedSerializer
from shelter.services import exchange_currency
from shelter.validators import validator_scam_words


class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validator_scam_words])

    class Meta:
        model = Dog
        fields = '__all__'


class DogDetailSerializer(serializers.ModelSerializer):
    #отдельный сериализатор чтобы в детальном представлении выводилось только имя и порода
    breed = BreedDetailSerializer() # так бы мы вывели всю инфу об этой породе
    ## same_breed_dogs = serializers.IntegerField(source='filter()')
    same_breed_dogs = serializers.SerializerMethodField()
    eur_price = serializers.SerializerMethodField()
    usd_price = serializers.SerializerMethodField()
    # breed = BreedSerializer()

    def get_eur_price(self, instance):
        return exchange_currency(instance.price, 'EUR')

    def get_usd_price(self, instance):
        return exchange_currency(instance.price, 'USD')


    def get_same_breed_dogs(self, instance):
        qty = Dog.objects.filter(breed=instance.breed.id).count()
        return qty

    class Meta:
        model = Dog
        # fields = ('name', 'breed', 'eur_price', 'usd_price', 'price')
        fields = ('name', 'breed', 'same_breed_dogs', 'eur_price', 'usd_price')
