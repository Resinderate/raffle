# Generated by Django 3.0 on 2019-12-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
