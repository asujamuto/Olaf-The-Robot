# Generated by Django 2.2.5 on 2022-10-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='bot_message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='user_message',
            field=models.CharField(max_length=200),
        ),
    ]
