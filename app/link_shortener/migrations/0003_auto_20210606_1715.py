# Generated by Django 2.1.15 on 2021-06-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0002_auto_20210605_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkshortener',
            old_name='hash_link',
            new_name='hash',
        ),
        migrations.AlterField(
            model_name='linkshortener',
            name='full_link',
            field=models.TextField(unique=True),
        ),
    ]