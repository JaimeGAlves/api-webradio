# Generated by Django 5.0.6 on 2024-07-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0006_alter_sponsor_options_remove_sponsor_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
