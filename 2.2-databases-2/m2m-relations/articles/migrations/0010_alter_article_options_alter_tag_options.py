# Generated by Django 5.0.3 on 2024-03-20 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
