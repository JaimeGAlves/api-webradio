# Generated by Django 5.0.6 on 2024-06-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['display_order']},
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='display_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='image_mobile',
            field=models.ImageField(default='/imagedefault.png', upload_to='sponsors/mobile/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='image_web',
            field=models.ImageField(default='/imagedefaultweb.png', upload_to='sponsors/web/'),
            preserve_default=False,
        ),
    ]
