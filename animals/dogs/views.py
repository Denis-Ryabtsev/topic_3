from rest_framework import viewsets
from django.db.models import Avg, Count, OuterRef, Subquery

from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    API-представление для управления породами собак

    ViewSet выполняет CRUD-операции над объектами породы (Breed)
    Добавляет аннотацию `dog_count` для количества собак данной породы

    Attributes:
        queryset (QuerySet): Список объектов породы с аннотацией `dog_count`.
        serializer_class (Serializer): Сериализатор для породы.
    """

    queryset = Breed.objects.annotate(
        dog_count=Count('breeds')
    )
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    API-представление для управления собаками

    ViewSet выполняет CRUD-операции над объектами собак (Dog)
    Добавляет аннотацию `avg_age` для среднего возраста собак данной породы

    Attributes:
        queryset (QuerySet): Список объектов собак с аннотацией `avg_age`.
        serializer_class (Serializer): Сериализатор для собаки.
    """

    queryset = Dog.objects.annotate(
        avg_age=Subquery(
            Dog.objects.filter(
                breed=OuterRef('breed')
            ).values(
                'breed'
            ).annotate(
                temp_age=Avg('age')
            ).values(
                'temp_age'
            )[:1]
        )
    )
    serializer_class = DogSerializer
