# Generated by Django 2.1 on 2018-08-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandejao', '0004_auto_20180830_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refeicao',
            name='data',
            field=models.DateField(verbose_name='dataRefeicao'),
        ),
    ]
