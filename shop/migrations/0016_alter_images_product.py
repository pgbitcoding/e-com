# Generated by Django 4.2.2 on 2023-06-28 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0015_category_banner_category_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="images",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="shop.product",
            ),
        ),
    ]
