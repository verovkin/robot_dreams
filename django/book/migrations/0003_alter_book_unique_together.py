# Generated by Django 4.2 on 2023-04-15 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_table'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
    ]