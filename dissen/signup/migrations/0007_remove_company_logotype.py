# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_auto_20160920_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logotype',
        ),
    ]
