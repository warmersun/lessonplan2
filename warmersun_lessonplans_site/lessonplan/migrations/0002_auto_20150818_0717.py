# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplanpage',
            name='introduction_length',
            field=models.PositiveSmallIntegerField(help_text='in minutes Including introduction of theme, new tool and design challenge'),
        ),
    ]
