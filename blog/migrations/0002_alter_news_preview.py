# Generated by Django 3.2.10 on 2021-12-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='preview',
            field=models.ImageField(null=True, upload_to='static/news-img/', verbose_name='Изображение'),
        ),
    ]