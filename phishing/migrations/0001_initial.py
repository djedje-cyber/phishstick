# Generated by Django 4.0.4 on 2022-05-23 16:01

from django.db import migrations, models
import phishing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.CharField(default=phishing.models.generate_id, max_length=32, primary_key=True, serialize=False)),
                ('sent_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('opened_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('clicked_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('phished_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TargetPool',
            fields=[
                ('id', models.CharField(default=phishing.models.generate_id, max_length=32, primary_key=True, serialize=False)),
                ('group', models.CharField(max_length=256)),
                ('template', models.CharField(max_length=256)),
                ('sent_count', models.PositiveIntegerField(default=0)),
                ('opened_count', models.PositiveIntegerField(default=0)),
                ('clicked_count', models.PositiveIntegerField(default=0)),
                ('phished_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]