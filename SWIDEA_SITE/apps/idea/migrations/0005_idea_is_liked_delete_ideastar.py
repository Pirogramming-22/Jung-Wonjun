# Generated by Django 5.1.4 on 2025-01-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0004_ideastar'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='IdeaStar',
        ),
    ]
