# Generated by Django 3.2 on 2022-06-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promoted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
