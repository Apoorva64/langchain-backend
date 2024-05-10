# Generated by Django 5.0.4 on 2024-05-09 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChainNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chain')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.node')),
            ],
        ),
        migrations.AddField(
            model_name='chain',
            name='nodes',
            field=models.ManyToManyField(through='api.ChainNode', to='api.node'),
        ),
    ]
