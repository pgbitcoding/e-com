# Generated by Django 4.2.1 on 2023-06-27 05:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_category_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="quantity",
        ),
    ]