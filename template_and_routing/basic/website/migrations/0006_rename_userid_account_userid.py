# Generated by Django 4.1.2 on 2022-11-22 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_user_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='userid',
            new_name='userID',
        ),
    ]