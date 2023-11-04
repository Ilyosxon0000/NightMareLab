# Generated by Django 4.2.7 on 2023-11-04 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pay', models.CharField(choices=[('TO_COMPANY', 'TO_COMPANY'), ('TO_OWNER', 'TO_OWNER')], default='TO_COMPANY', max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('animation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users_animations', to='product.animation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_animations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]