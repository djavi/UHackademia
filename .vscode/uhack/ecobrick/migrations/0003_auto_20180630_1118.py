# Generated by Django 2.0.3 on 2018-06-30 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecobrick', '0002_auto_20180630_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myreward',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecobrick.UserDetail'),
        ),
    ]
