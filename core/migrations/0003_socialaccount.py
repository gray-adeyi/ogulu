# Generated by Django 3.2.9 on 2021-11-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211119_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('twitter', 'Twitter'), ('tiktok', 'Tik Tok'), ('telegram', 'Telegram')], max_length=15)),
                ('link', models.URLField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='core.myinformation')),
            ],
        ),
    ]
