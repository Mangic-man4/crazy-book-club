# Generated by Django 4.2.6 on 2023-11-13 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_alter_review_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
    ]
