# Generated by Django 4.1.2 on 2022-11-01 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s_card_econ_app_03', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart',
            new_name='cart_id',
        ),
    ]
