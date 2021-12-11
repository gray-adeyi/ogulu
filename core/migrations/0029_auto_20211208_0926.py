# Generated by Django 3.2.9 on 2021-12-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_rename_transation_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myimage',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='picturecategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]