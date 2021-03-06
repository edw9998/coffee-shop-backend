# Generated by Django 4.0.5 on 2022-06-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HTTP_Method', models.CharField(max_length=1000)),
                ('URL_Endpoint', models.CharField(max_length=1000)),
                ('Request_Body', models.CharField(max_length=1000)),
                ('Response_Body', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
