# Generated by Django 4.2.7 on 2023-11-02 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_rename_file_animation_file30_animation_file60'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.FileField(upload_to='company/model/%y/%m/%d/')),
                ('logo', models.FileField(upload_to='company/logo/%y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='animation',
            name='file30',
            field=models.FileField(upload_to='animations/file30/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='animation',
            name='file60',
            field=models.FileField(upload_to='animations/file60/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type_pay',
            field=models.CharField(choices=[('TO_COMPANY', 'TO_COMPANY'), ('TO_OWNER', 'TO_OWNER')], default='TO_COMPANY', max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='webapp.subcategory'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='webapp.requesttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to='webapp.usertype'),
            preserve_default=False,
        ),
    ]
