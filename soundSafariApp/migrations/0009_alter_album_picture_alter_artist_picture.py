# Generated by Django 4.0.6 on 2024-03-22 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundSafariApp', '0008_remove_review_album_remove_review_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
