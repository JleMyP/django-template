# Generated by Django 2.2.6 on 2019-10-27 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191027_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('can_edit_customuser_settings', 'Can edit user settings')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]