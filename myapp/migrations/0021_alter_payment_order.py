# Generated by Django 3.2.14 on 2022-11-08 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='ORDER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order_sub'),
        ),
    ]
