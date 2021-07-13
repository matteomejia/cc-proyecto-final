# Generated by Django 3.2.5 on 2021-07-12 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='topics', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=254, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.FloatField(verbose_name='price')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='discount price')),
                ('image', models.ImageField(upload_to='workshops', verbose_name='image')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('hours', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('weeks', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('schedule', models.TextField(blank=True, null=True)),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'beginner'), (2, 'intermediate'), (3, 'advanced')], default=1, verbose_name='level')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'public'), (2, 'private'), (3, 'inactive')], default=1, verbose_name='status')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshops.topic', verbose_name='topic')),
            ],
            options={
                'verbose_name': 'workshop',
                'verbose_name_plural': 'workshops',
            },
        ),
    ]
