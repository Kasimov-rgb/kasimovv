# Generated by Django 5.0.3 on 2024-04-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_buyer',
            field=models.BooleanField(default=False, verbose_name='Покупатель'),
        ),
    ]