# Generated by Django 2.2.4 on 2019-08-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meizifilter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediadate',
            name='domain',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
