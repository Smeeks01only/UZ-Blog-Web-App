# Generated by Django 4.2.7 on 2023-11-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='img/%y'),
        ),
    ]
