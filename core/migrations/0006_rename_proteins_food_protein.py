# Generated by Django 4.2 on 2023-06-27 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_food_snack_type_alter_food_calories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='proteins',
            new_name='protein',
        ),
    ]
