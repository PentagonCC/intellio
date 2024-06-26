# Generated by Django 4.1.13 on 2024-05-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('source', models.URLField()),
                ('image_url', models.URLField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
