# Generated by Django 5.1.2 on 2025-01-23 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(upload_to='noticias/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fontes', to='notices.noticias')),
            ],
        ),
    ]
