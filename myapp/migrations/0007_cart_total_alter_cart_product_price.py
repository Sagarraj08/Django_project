# Generated by Django 4.1.7 on 2023-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="total",
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name="cart",
            name="product_price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
