# Generated by Django 3.2.7 on 2021-09-25 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_merge_20210925_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='result',
            field=models.CharField(choices=[('fire', 'FIRE족'), ('yolo', 'YOLO족'), ('null', '미선택')], default='null', max_length=5),
        ),
    ]
