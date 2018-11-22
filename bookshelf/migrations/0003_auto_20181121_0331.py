# Generated by Django 2.1.3 on 2018-11-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_auto_20181121_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]
