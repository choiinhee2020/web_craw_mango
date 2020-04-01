# Generated by Django 2.2.11 on 2020-04-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='parking',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='parking_text',
            field=models.CharField(blank=True, default='주차여부 알수 없음', max_length=100, verbose_name='주차여부'),
        ),
    ]
