# Generated by Django 4.0.1 on 2022-01-29 08:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=255)),
                ('comment_date', models.DateField(verbose_name=datetime.datetime(2022, 1, 29, 0, 18, 44, 244757))),
                ('snippet_rating', models.SmallIntegerField()),
                ('discussion_text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'comment',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snippet_title', models.CharField(max_length=255)),
                ('snippet_entrydate', models.DateField(verbose_name=datetime.datetime(2022, 1, 29, 0, 18, 44, 244757))),
                ('reference_url', models.URLField(blank=True, null=True)),
                ('code_snippet', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'snippets',
                'db_table': 'snippet',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('tag_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
                'db_table': 'tag',
            },
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='snippet',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Club.tag'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.snippet'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
