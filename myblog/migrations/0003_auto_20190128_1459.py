# Generated by Django 2.0.10 on 2019-01-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20190128_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
