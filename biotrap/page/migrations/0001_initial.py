# Generated by Django 2.2.12 on 2020-08-05 16:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de edición')),
            ],
            options={
                'verbose_name': 'página',
                'verbose_name_plural': 'páginas',
                'ordering': ['title'],
            },
        ),
    ]
