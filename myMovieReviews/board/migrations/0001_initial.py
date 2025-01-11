# Generated by Django 5.1.4 on 2025-01-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.TextField()),
                ('genre', models.TextField()),
                ('score', models.TextField()),
                ('director', models.TextField()),
                ('actor', models.TextField()),
                ('runtime', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
