# Generated by Django 3.2.2 on 2021-05-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='available',
            field=models.IntegerField(null=True),
        ),
    ]
