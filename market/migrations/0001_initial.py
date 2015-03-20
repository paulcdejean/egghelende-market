# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=255)),
                ('my_price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('in_stock', models.IntegerField()),
                ('in_build', models.IntegerField()),
                ('in_need', models.IntegerField()),
                ('total_sold', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
