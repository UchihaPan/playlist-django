# Generated by Django 3.1.3 on 2020-11-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoshandler', '0004_auto_20201112_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='url',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='youtube',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='wall',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
