# Generated by Django 4.0.6 on 2022-09-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppMusica', '0003_alter_blogmetal_options_alter_blogrock_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='blogmetal',
            name='subtitulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to=settings.AUTH_USER_MODEL),
        ),
    ]