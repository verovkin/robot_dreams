from django.db import models


class Purchase(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    book_id = models.ForeignKey('book.Book', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']
