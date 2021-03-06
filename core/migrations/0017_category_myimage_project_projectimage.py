# Generated by Django 3.2.9 on 2021-11-20 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=50)),
                ('client_logo', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress')], default='in_progress', max_length=15)),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('categories', models.ManyToManyField(to='core.Category')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.myinformation')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('categories', models.ManyToManyField(to='core.Category')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='core.myinformation')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
