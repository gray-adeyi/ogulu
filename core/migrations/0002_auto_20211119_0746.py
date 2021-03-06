# Generated by Django 3.2.9 on 2021-11-19 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinformation',
            name='city',
            field=models.CharField(default='Ado-Ekiti, Nigeria', help_text="Where you're based at the moment", max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myinformation',
            name='display_text',
            field=models.TextField(default='The <span>top</span> feels so much better than the bottom.', help_text="What text should appear on your site's landing page", max_length=200),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='core.myinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=15)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='core.myinformation')),
            ],
        ),
    ]
