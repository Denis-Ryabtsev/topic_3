from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


SIZE=[
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large")
]

class Breed(models.Model):
    """Модель породы собак

    Содержит информацию о породе и ее характеристиках

    Attributes:
        name (CharField): Название породы
        size (CharField): Размер породы (Tiny, Small, Medium, Large).
        friendliness (IntegerField): Дружелюбие (1-5).
        trainability (IntegerField): Обучаемость (1-5).
        shedding_amount (IntegerField): Уровень линьки (1-5).
        exercise_needs (IntegerField): Необходимость физической нагрузки (1-5).
    """

    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=20
    )
    size = models.CharField(
        max_length=7,
        choices=SIZE
    )
    friendliness = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    trainability = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    shedding_amount = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    exercise_needs = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
            """Возвращает строковое представление объекта"""

            return self.name
    

    class Meta:
        """Метаданные для модели"""

        db_table = 'breed'


class Dog(models.Model):
    """Модель собаки

    Описывает отдельную собаку и ее характеристики

    Attributes:
        name (CharField): Имя собаки
        age (IntegerField): Возраст собаки
        breed (ForeignKey): Связь с породой
        gender (CharField): Пол собаки
        color (CharField): Окрас собаки
        favorite_food (CharField): Любимая еда
        favorite_toy (CharField): Любимая игрушка
    """

    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100
    )
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='breeds'
    )
    gender = models.CharField(
        max_length=10
    )
    color = models.CharField(
        max_length=30
    )
    favorite_food = models.CharField(
        max_length=40
    )
    favorite_toy = models.CharField(
        max_length=40
    )


    class Meta:
        """Метаданные для модели Dog."""
        
        db_table = 'dog'