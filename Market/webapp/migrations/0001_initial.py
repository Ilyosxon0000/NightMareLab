# Generated by Django 4.2.7 on 2023-11-01 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='animations/file/%y/%m/%d/')),
                ('price', models.IntegerField(default=0)),
                ('preview', models.FileField(upload_to='animations/preview/%y/%m/%d/')),
                ('downloads', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BodyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='webapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('image', models.FileField(blank=True, null=True, upload_to='users/%y/%m/%d/')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='webapp.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='webapp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pay', models.CharField(choices=[('TO_COMPANY', 'TO_COMPANY'), ('TO_USER', 'TO_USER')], default='TO_COMPANY', max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('animation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users_animations', to='webapp.animation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_animations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='animation',
            name='body_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animations', to='webapp.bodycategory'),
        ),
        migrations.AddField(
            model_name='animation',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='my_owner_animations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='animation',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animations', to='webapp.tag'),
        ),
    ]