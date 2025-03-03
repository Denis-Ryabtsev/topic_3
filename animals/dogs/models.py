from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# name (строка символов)
# size (строка символов) [должно принимать значения Tiny, Small, Medium, Large]
# friendliness (поле целого числа) [должно принимать значения от 1 до 5]
# trainability (поле целого числа) [должно принимать значения от 1 до 5]
# shedding_amount (поле целого числа) [должно принимать значения от 1 до 5]
# exercise_needs (поле целого числа) [должно принимать значения от 1 до 5]

SIZE=[
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large")
]

class Breed(models.Model):
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

    class Meta:
        db_table = 'breed'


class Dog(models.Model):
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
        db_table = 'dog'

