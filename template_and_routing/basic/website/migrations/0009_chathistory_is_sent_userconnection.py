# Generated by Django 4.1.2 on 2022-11-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_account_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connected', models.CharField(max_length=128)),
                ('is_started', models.BooleanField(default=False)),
                ('userid', models.CharField(max_length=6)),
                ('connectionid', models.CharField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.account')),
            ],
        ),
    ]