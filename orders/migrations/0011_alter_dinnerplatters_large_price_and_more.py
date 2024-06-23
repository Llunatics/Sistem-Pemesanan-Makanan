# Generated by Django 4.2.1 on 2024-06-23 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0010_alter_category_options_alter_dinnerplatters_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dinnerplatters",
            name="large_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="dinnerplatters",
            name="small_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="pasta",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="regularpizza",
            name="large_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="regularpizza",
            name="small_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="salad",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="sicilianpizza",
            name="large_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="sicilianpizza",
            name="small_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="sub",
            name="large_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="sub",
            name="small_price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="userorder",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]