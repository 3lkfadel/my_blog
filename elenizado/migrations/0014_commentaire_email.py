# Generated by Django 2.2.12 on 2020-07-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0013_textes'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
