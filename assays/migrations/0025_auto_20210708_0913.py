# Generated by Django 2.2 on 2021-07-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0024_auto_20210708_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='mid',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
