# Generated by Django 3.0.2 on 2020-02-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_coupon_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
    ]
