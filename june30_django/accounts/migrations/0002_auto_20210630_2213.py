# Generated by Django 3.2.4 on 2021-06-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='schoolfile',
        ),
        migrations.AddField(
            model_name='education',
            name='college_certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='education',
            name='highschool_certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='education',
            name='school_certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
