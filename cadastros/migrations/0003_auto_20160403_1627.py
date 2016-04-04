# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Pessoa'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano_fabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano_modelo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Marca'),
        ),
    ]
