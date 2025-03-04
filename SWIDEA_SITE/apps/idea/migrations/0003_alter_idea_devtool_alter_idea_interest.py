# Generated by Django 5.1.4 on 2025-01-15 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_idea_created_at'),
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='tool.tool', verbose_name='예상 개발툴:'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='interest',
            field=models.IntegerField(verbose_name='아이디어 관심도:'),
        ),
    ]
