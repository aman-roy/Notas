# Generated by Django 2.2.4 on 2019-09-14 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('napp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='napp.Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='notes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='napp.Notes'),
        ),
    ]