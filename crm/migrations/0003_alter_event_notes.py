# Generated by Django 4.2 on 2023-05-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_user_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]