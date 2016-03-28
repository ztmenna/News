# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publicationDate', models.DateTimeField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='feed',
            field=models.ForeignKey(to='news.Feed'),
        ),
    ]
