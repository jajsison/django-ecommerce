# Generated by Django 4.1.2 on 2023-01-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_banner_options_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '3. Brands'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '4. Product'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '5. ProductAttributes'},
        ),
        migrations.AddField(
            model_name='productattribute',
            name='image',
            field=models.ImageField(null=True, upload_to='product_imgs/'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='banner_imgs/'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
