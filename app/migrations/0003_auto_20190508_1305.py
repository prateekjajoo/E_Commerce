# Generated by Django 2.0 on 2019-05-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Mobile', 'Mobile'), ('television', 'television'), ('refrigerator', 'refrigerator')], default='None', max_length=30, null=True),
        ),
    ]
