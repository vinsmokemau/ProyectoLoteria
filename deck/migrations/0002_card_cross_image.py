# Generated by Django 2.2.4 on 2019-09-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cross_image',
            field=models.ImageField(null=True, upload_to='cross_images', verbose_name='imagen'),
        ),
    ]
