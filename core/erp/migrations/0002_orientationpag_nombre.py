# Generated by Django 3.1.6 on 2021-05-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientationpag',
            name='nombre',
            field=models.CharField(default=1, max_length=150, unique=True, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
