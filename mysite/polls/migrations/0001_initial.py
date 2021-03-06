# Generated by Django 4.0.1 on 2022-02-01 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogada', models.CharField(default='Esta é a jogada Nº: ', max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('banca_inicial', models.FloatField(default=0)),
                ('stopgain', models.IntegerField(default=0)),
                ('stoploss', models.IntegerField(default=0)),
                ('banca_atual', models.FloatField(default=0)),
                ('green', models.FloatField(default=0)),
                ('red', models.FloatField(default=0)),
                ('primeira_entrada', models.FloatField()),
                ('created', models.TimeField(auto_now_add=True)),
                ('rendimento', models.FloatField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
