# Generated by Django 4.2.7 on 2023-12-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_user_sneaker_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='debut_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user_sneaker',
            name='debut_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user_sneaker',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
