# Generated by Django 4.1 on 2023-02-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('subject', models.CharField(max_length=20, null=True)),
                ('message', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]