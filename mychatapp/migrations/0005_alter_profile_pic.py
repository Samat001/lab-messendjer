# Generated by Django 4.1.7 on 2023-04-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0004_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='img'),
        ),
    ]