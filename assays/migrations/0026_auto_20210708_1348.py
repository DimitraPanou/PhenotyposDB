# Generated by Django 2.2 on 2021-07-08 13:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0025_auto_20210708_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
