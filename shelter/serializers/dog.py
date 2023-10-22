
from rest_framework import serializers

from shelter.models import Dog


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'
        