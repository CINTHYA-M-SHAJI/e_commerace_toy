# Generated by Django 3.2.2 on 2023-03-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_App', '0002_auto_20230312_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Availabilty',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
