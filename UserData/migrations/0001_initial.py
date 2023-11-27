# Generated by Django 4.2.7 on 2023-11-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'User Information',
            },
        ),
    ]
