# Generated by Django 5.0.3 on 2024-03-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='Tarixiy'),
            preserve_default=False,
        ),
    ]
