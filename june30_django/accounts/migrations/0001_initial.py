# Generated by Django 3.2.4 on 2021-06-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=40)),
                ('schoolfile', models.FileField(upload_to='')),
                ('highschool', models.CharField(max_length=40)),
                ('college', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=40)),
                ('schoolfile', models.FileField(upload_to='')),
                ('highschool', models.CharField(max_length=40)),
                ('college', models.CharField(max_length=40)),
            ],
        ),
    ]
