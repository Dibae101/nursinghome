# Generated by Django 3.2.3 on 2021-06-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210610_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, default='1234'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='zip_code_1',
            field=models.PositiveIntegerField(blank=True, default='1234'),
        ),
    ]
