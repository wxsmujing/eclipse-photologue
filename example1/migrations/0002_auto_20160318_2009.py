# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTextMap',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('PhotoTextMap_texttitle', models.CharField(max_length=30)),
                ('PhotoTextMap_phototype', models.CharField(max_length=30)),
                ('PhotoTextMap_phototitle', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='text',
            old_name='text_unique',
            new_name='photo_name',
        ),
    ]
