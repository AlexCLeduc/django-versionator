# Generated by Django 2.2.11 on 2021-01-26 21:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='sample_app.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='BookVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='hypothetical last edit date')),
                ('title', models.CharField(max_length=250)),
                ('tags', models.TextField(default='[]')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sample_app.Author', verbose_name='author')),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('eternal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='sample_app.Book')),
            ],
            options={
                'ordering': ['business_date'],
                'get_latest_by': 'business_date',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='sample_app.Tag'),
        ),
        migrations.CreateModel(
            name='AuthorVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='hypothetical last edit date')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('eternal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='sample_app.Author')),
            ],
            options={
                'ordering': ['business_date'],
                'get_latest_by': 'business_date',
                'abstract': False,
            },
        ),
    ]
