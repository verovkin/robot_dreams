from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
import datetime


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(datetime.date.today().year)])
    price = models.FloatField(null=True)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.id}. {self.title}, {self.author}, {self.year} - {self.price}'


    def get_absolute_url(self):
        return reverse('books-detail', args=[self.id])