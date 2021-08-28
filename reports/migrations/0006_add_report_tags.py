# Generated by Django 3.0 on 2021-08-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_add_base_dataset_20200620_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='reports.Tag'),
        ),
    ]