# Generated by Django 4.1.1 on 2022-09-16 10:22

from django.db import migrations
import film.models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rate',
            field=film.models.IntegerRangeField(blank=True, default=0, null=True),
        ),
    ]
