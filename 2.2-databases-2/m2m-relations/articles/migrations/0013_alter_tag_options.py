# Generated by Django 5.0.3 on 2024-03-20 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
