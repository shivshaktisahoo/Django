# Generated by Django 3.2.4 on 2021-07-06 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacationtrip',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='vacationtrip',
            old_name='lname',
            new_name='last_name',
        ),
    ]
