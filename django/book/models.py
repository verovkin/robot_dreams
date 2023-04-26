from django.db import models
from django.core.validators import MaxValueValidator
import datetime


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(datetime.date.today().year)])
    price = models.FloatField(null=True)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author',)
