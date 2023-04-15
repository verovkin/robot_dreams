# Generated by Django 4.2 on 2023-04-14 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2023)])),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
