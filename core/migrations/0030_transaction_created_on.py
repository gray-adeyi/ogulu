# Generated by Django 3.2.9 on 2021-12-08 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20211208_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 8, 8, 28, 48, 620406, tzinfo=utc)),
            preserve_default=False,
        ),
    ]