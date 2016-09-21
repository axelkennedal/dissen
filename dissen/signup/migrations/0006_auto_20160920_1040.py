# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_fair_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='area_of_business',
            field=models.CharField(default='Pick one', choices=[('finance', 'Finance'), ('appdev', 'App Development'), ('consulting', 'Consulting'), ('entertainment', 'Entertainment'), ('comm', 'Communication'), ('it', 'IT Services'), ('prodev', 'Product Development'), ('info', 'Information'), ('edu', 'Education'), ('data', 'Data & Search'), ('fash', 'Fashion'), ('sec', 'Security'), ('man', 'Management')], max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='logotype',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='priority',
            field=models.CharField(default=('low', 'LOW'), choices=[('low', 'LOW'), ('mid', 'MID'), ('high', 'HIGH')], max_length=10),
        ),
        migrations.AlterField(
            model_name='companystatus',
            name='STATUS',
            field=models.CharField(default=('notcontacted', 'Not Contacted'), choices=[('notcontacted', 'Not Contacted'), ('contacted', 'Contacted - Waiting to sign up'), ('signedup', 'Signed Up - Waiting for contract to be signed'), ('contractsigned', 'Contract Signed'), ('dec', 'Declined')], max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('lunch', 'Lunch lecture'), ('pub', 'Pub'), ('other', 'Other')], max_length=100),
        ),
    ]
