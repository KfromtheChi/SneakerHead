# Generated by Django 4.2.7 on 2023-12-21 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_icon_title_icon_sneaker_rename_name_icon_why_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_sneaker',
            name='price',
            field=models.TextField(max_length=100),
        ),
    ]
