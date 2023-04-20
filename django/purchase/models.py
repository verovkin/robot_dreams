from django.db import models
from datetime import datetime

class Purchase(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    book_id = models.ForeignKey('book.Book', on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'purchase'
        ordering = ['-purchase_date']
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        print(type(self.purchase_date))
        return f'{self.id}, {self.purchase_date.strftime("%m/%d/%Y, %H:%M:%S")}, {self.book_id.title}, {self.user_id.first_name} {self.user_id.last_name} - {self.book_id.price}'
        # return f'{self.id}, , {self.book_id.title}, {self.user_id.first_name} {self.user_id.last_name} - {self.book_id.price}'
