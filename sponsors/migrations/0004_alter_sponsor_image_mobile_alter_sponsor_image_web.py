# Generated by Django 5.0.6 on 2024-06-22 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_alter_sponsor_image_mobile_alter_sponsor_image_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='image_mobile',
            field=models.ImageField(upload_to='sponsors/mobile/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image_web',
            field=models.ImageField(upload_to='sponsors/web/'),
        ),
    ]
