# Generated by Django 3.0.6 on 2020-05-22 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
    ]
