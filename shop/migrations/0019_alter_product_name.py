# Generated by Django 4.2.2 on 2023-06-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0018_alter_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]