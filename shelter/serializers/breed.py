from rest_framework import serializers

from shelter.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
