# Generated by Django 4.0 on 2023-08-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookversion',
            name='tags',
            field=models.TextField(default='[]'),
        ),
    ]