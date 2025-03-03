from rest_framework import serializers
from dogs.models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all()
    )

    class Meta:
        model = Dog
        fields = '__all__'