# Generated by Django 2.2.12 on 2020-07-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0014_commentaire_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='reponsecommentaire',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
