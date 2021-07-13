# Generated by Django 3.2.5 on 2021-07-13 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='last name')),
                ('country', django_countries.fields.CountryField(default='PE', max_length=2, verbose_name='country')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'parent'), (2, 'teacher'), (3, 'adult student')], default=1, verbose_name='role')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='phone')),
                ('school', models.CharField(blank=True, max_length=254, null=True, verbose_name='school')),
                ('document', models.CharField(blank=True, max_length=100, null=True, verbose_name='document')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['first_name', 'last_name'], unique=True)),
                ('first_name', models.CharField(max_length=254, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=254, verbose_name='last name')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('school', models.CharField(max_length=254, verbose_name='school')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='parent')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
    ]
