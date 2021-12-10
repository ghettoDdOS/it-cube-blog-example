# Generated by Django 3.2.10 on 2021-12-10 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('preview', models.ImageField(null=True, upload_to='news-img/', verbose_name='Изображение')),
                ('date_of_publication', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('text', models.TextField(null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['date_of_publication'],
            },
        ),
    ]
