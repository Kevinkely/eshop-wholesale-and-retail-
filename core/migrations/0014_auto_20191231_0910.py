# Generated by Django 2.2 on 2019-12-31 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_order_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='size',
            new_name='item_size',
        ),
        migrations.RenameField(
            model_name='wholesaler',
            old_name='size',
            new_name='wholesaler_size',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.AddField(
            model_name='order',
            name='item_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size', to='core.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='wholesaler_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size', to='core.Wholesaler'),
        ),
    ]
