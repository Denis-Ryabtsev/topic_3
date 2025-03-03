from rest_framework import serializers
from django.db.models import Avg

from dogs.models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Breed
        К модели Breed добавляет поле dog_count для отображения количества собак породы
    
    Attributes:
        dog_count (int): Количество собак данной породы

    """
    
    dog_count: int = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        """Метаданные для сериализатора"""

        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Dog.

    Добавляет дополнительные поля:
        - `avg_age`: Средний возраст собак данной породы.
        - `breed_count`: Количество собак той же породы.
        - `breed`: Представление породы через PrimaryKey.

    Attributes:
        avg_age (float): Средний возраст собак данной породы.
        breed (int): ID породы.
        breed_count (int): Количество собак той же породы.
    """

    avg_age: float = serializers.SerializerMethodField()
    breed: str = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all()
    )
    breed_count: int = serializers.SerializerMethodField() 

    class Meta:
        """Метаданные для сериализатора"""

        model = Dog
        fields = '__all__'
        extra_fields = [
            'avg_age',
            'breed',
            'breed_count'
        ]
    

    def get_avg_age(self, obj: Dog) -> int:
        """Вычисляет средний возраст собак данной породы.

        Args:
            obj (Dog): Объект модели Dog.

        Returns:
            float: Средний возраст собак породы (или 0, если данных нет).
        """

        temp_age = Dog.objects.filter(breed=obj.breed).aggregate(
            Avg('age')
        )['age__avg']

        return temp_age if temp_age else 0

    def get_breed_count(self, obj: Dog) -> int:
        """Вычисляет количество собак той же породы.

        Args:
            obj (Dog): Объект модели Dog.

        Returns:
            int: Количество собак данной породы.
        """

        return Dog.objects.filter(breed=obj.breed).count()