# Generated by Django 4.0.1 on 2022-01-29 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0005_alter_comment_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 1, 29, 0, 51, 39, 288552)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='snippet_entrydate',
            field=models.DateField(verbose_name=datetime.datetime(2022, 1, 29, 0, 51, 39, 287555)),
        ),
    ]
