# Generated by Django 3.1.2 on 2020-10-28 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20201026_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스트캠퍼스 사용자'},
        ),
    ]