# Generated by Django 2.2 on 2019-04-14 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_auto_20190413_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='autor',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data dodania'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'], verbose_name='Uproszczona nazwa'),
        ),
    ]
