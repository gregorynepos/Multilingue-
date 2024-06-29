# Generated by Django 5.0.6 on 2024-06-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multilang_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_fr',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_it',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_pt',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_fr',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_it',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_pt',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
    ]
