# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 00:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerTicket',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multitable.Ticket')),
                ('product', models.TextField(blank=True)),
            ],
            bases=('multitable.ticket',),
        ),
        migrations.CreateModel(
            name='InternalTicket',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multitable.Ticket')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('multitable.ticket',),
        ),
    ]
