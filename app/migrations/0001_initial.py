# Generated by Django 2.0 on 2019-05-08 05:41

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Mobile', 'Mobile'), ('television', 'television'), ('refrigerator', 'refrigerator')], default='None', max_length=10, null=True)),
                ('company_name', models.CharField(max_length=50)),
                ('specification', tinymce.models.HTMLField(blank=True, default='')),
                ('prize', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='None', max_length=10, null=True)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
