# Generated by Django 2.2.12 on 2020-06-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0008_auto_20200629_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.URLField(),
        ),
    ]
