# Generated by Django 4.2 on 2023-04-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Buyer',
                'verbose_name_plural': 'Buyers',
                'db_table': 'users',
            },
        ),
    ]
