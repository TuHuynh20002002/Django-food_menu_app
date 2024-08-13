# Generated by Django 5.0.7 on 2024-07-14 17:27

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=timezone.now, editable=False)),
            ],
        ),
    ]
