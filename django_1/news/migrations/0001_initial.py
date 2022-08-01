# Generated by Django 4.0.6 on 2022-07-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('shortdiscription', models.CharField(max_length=250, verbose_name='anons')),
                ('full_text', models.TextField(verbose_name='article')),
                ('date', models.DateTimeField(verbose_name='date of publishing')),
            ],
        ),
    ]
