# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplan', '0003_homepage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='BlogPage',
        ),
    ]
