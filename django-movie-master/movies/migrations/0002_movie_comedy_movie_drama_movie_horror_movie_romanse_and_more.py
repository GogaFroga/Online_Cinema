# Generated by Django 4.0.6 on 2022-07-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='comedy',
            field=models.BooleanField(default=False, verbose_name='Жанр - комедия'),
        ),
        migrations.AddField(
            model_name='movie',
            name='drama',
            field=models.BooleanField(default=False, verbose_name='Жанр - мелодрама'),
        ),
        migrations.AddField(
            model_name='movie',
            name='horror',
            field=models.BooleanField(default=False, verbose_name='Жанр - ужасы'),
        ),
        migrations.AddField(
            model_name='movie',
            name='romanse',
            field=models.BooleanField(default=False, verbose_name='Жанр - мелодрамма'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cartoons',
            field=models.BooleanField(default=False, verbose_name='Мультфильм'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='films',
            field=models.BooleanField(default=False, verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movie', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя фильма'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='soap_opera',
            field=models.BooleanField(default=False, verbose_name='Сериал'),
        ),
    ]