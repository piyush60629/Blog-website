# Generated by Django 5.0.1 on 2024-01-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Cat', models.CharField(max_length=60)),
            ],
        ),
    ]
