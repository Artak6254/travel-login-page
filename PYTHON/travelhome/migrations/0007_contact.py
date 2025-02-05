# Generated by Django 5.1.4 on 2025-01-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelhome', '0006_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_svg', models.FileField(upload_to='svgs/')),
                ('email_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('people_number', models.IntegerField()),
                ('subjact', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
