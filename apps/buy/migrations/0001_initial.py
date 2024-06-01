# Generated by Django 5.0.3 on 2024-05-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('card_pin', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]
