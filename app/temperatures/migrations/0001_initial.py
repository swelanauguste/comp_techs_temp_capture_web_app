# Generated by Django 3.2.7 on 2021-11-29 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nic_no', models.CharField(max_length=8, verbose_name='NIC')),
                ('dob', models.DateField(verbose_name='DOB')),
                ('address', models.CharField(help_text='Derriere Fort, the Morne', max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='districts', to='temperatures.district')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to='temperatures.organization')),
            ],
            options={
                'ordering': ('-temperature',),
            },
        ),
    ]