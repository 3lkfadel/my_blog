# Generated by Django 2.2.12 on 2020-07-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0015_reponsecommentaire_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reponsecommentaire',
            old_name='Commentaires',
            new_name='commentaires',
        ),
    ]
