# Generated by Django 4.2.7 on 2023-12-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_icon_debut_year_alter_user_sneaker_debut_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='debut_year',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='icon',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_sneaker',
            name='debut_year',
            field=models.CharField(max_length=100),
        ),
    ]
