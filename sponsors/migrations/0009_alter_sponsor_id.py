# Generated by Django 5.0.6 on 2024-07-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0008_alter_sponsor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
