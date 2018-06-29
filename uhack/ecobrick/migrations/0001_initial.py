# Generated by Django 2.0.3 on 2018-06-29 23:31

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
            name='Brick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brickWeight', models.PositiveIntegerField(default=0)),
                ('brickVolume', models.PositiveIntegerField(default=0)),
                ('brickPoint', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('barangay', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('long', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('contactNum', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewardName', models.CharField(max_length=250)),
                ('pointCost', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('contactNum', models.CharField(max_length=50)),
                ('userType', models.IntegerField(choices=[(0, 'Staff'), (1, 'Regular User')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
