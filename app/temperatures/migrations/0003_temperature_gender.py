# Generated by Django 3.2.7 on 2021-11-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperatures', '0002_auto_20211129_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
    ]
