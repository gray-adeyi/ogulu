# Generated by Django 3.2.9 on 2021-11-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211119_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(help_text='the name of the skill', max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.PositiveIntegerField(help_text='how good you are at doing it'),
        ),
    ]