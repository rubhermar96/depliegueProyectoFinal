# Generated by Django 3.2.2 on 2021-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_auto_20210514_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cvc',
            field=models.FileField(blank=True, null=True, upload_to='cvcusuarios', verbose_name='Curriculum'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
    ]
