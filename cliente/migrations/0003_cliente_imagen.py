# Generated by Django 4.2.5 on 2023-10-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
