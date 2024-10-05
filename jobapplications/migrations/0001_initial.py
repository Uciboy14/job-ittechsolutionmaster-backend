# Generated by Django 4.2.14 on 2024-10-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
