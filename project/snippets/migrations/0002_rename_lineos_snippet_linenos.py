# Generated by Django 5.0.6 on 2024-06-12 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineos',
            new_name='linenos',
        ),
    ]
