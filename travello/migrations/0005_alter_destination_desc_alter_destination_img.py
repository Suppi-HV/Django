# Generated by Django 5.1.5 on 2025-01-28 17:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_alter_destination_id_alter_destination_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
