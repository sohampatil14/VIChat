# Generated by Django 4.1.2 on 2022-11-29 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_chathistory_is_sent_userconnection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userconnection',
            old_name='connected',
            new_name='userconnected',
        ),
    ]
