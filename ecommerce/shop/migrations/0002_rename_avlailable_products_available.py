# Generated by Django 5.0 on 2024-02-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='avlailable',
            new_name='available',
        ),
    ]
