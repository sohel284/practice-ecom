# Generated by Django 2.2.7 on 2020-06-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20200626_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_password',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='old_password',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
