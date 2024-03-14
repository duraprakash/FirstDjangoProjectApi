# Generated by Django 5.0.3 on 2024-03-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('marital_status', models.BooleanField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
