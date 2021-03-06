# Generated by Django 2.0.5 on 2019-01-07 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0005_auto_20190107_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=20, unique=True)),
                ('verify', models.CharField(choices=[('no', 'no'), ('yes', 'yes')], default='no', max_length=3)),
                ('field_of_practice', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
