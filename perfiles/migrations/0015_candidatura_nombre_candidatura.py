# Generated by Django 3.2.2 on 2021-05-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0014_rename_candidaturas_candidatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='nombre_candidatura',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
