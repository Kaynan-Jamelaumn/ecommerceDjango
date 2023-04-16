# Generated by Django 3.2.13 on 2023-04-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariation_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsubcategories', to='product.subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subsubcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.subsubcategory'),
        ),
    ]
