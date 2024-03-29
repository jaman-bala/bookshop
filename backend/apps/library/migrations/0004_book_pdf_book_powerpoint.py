# Generated by Django 4.2.9 on 2024-01-18 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_video_alter_book_bookpage_alter_book_coverpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
        migrations.AddField(
            model_name='book',
            name='powerpoint',
            field=models.FileField(blank=True, null=True, upload_to='powerpoints/'),
        ),
    ]
