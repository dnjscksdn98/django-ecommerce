# Generated by Django 3.0.2 on 2020-02-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='fjsdklfjlksdjflkdsjlf fjsdlkfjlksdjfl fjdsklfjsldkf'),
            preserve_default=False,
        ),
    ]