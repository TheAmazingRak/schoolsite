# Generated by Django 2.2 on 2019-04-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Wyświetlenia'),
        ),
    ]
