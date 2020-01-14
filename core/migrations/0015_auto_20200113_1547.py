# Generated by Django 2.2 on 2020-01-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191231_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[('M', 'MEN'), ('W', 'WOMEN'), ('K/B', 'KIDS/BABY'), ('D', 'DISCOVER')], default=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('M', 'MEN'), ('W', 'WOMEN'), ('K/B', 'KIDS/BABY'), ('D', 'DISCOVER')], max_length=3),
        ),
        migrations.AlterField(
            model_name='wholesaler',
            name='category',
            field=models.CharField(choices=[('M', 'MEN'), ('W', 'WOMEN'), ('K/B', 'KIDS/BABY'), ('D', 'DISCOVER')], max_length=3),
        ),
    ]
