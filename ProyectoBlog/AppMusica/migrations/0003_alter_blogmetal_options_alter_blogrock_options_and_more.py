# Generated by Django 4.0.6 on 2022-09-19 22:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMusica', '0002_alter_comentario_nombre_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmetal',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterModelOptions(
            name='blogrock',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='blogmetal',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blogrock',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]