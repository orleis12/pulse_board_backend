# Generated by Django 5.1.3 on 2024-11-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='clicked_button_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='clicked_button_2',
            field=models.IntegerField(default=0),
        ),
    ]
