# Generated by Django 4.2.11 on 2024-05-22 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0004_rename_comuna_comunas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comunas',
            new_name='Comuna',
        ),
    ]