# Generated by Django 3.2.25 on 2024-09-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_language_language_name_case_insensitive_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(help_text='Select a language for this book', to='catalog.Language'),
        ),
    ]
