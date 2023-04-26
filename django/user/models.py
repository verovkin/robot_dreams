from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} - {self.age} y.o.'
