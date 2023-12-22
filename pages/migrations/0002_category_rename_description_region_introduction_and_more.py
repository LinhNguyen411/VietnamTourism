# Generated by Django 5.0 on 2023-12-22 06:49

import django.db.models.deletion
import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='region',
            old_name='description',
            new_name='introduction',
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pages.region'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='CityGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=pages.models.CityGallery.get_upload_path)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.city')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('banner', models.FileField(upload_to=pages.models.Destination.get_upload_path)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pages.category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pages.city')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=pages.models.DestinationGallery.get_upload_path)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.destination')),
            ],
        ),
    ]