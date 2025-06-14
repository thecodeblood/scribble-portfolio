# Generated by Django 5.2.2 on 2025-06-04 20:01

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('purchase_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-publication_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('excerpt', models.TextField(blank=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='main.blogcategory')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
