# Generated by Django 5.0.6 on 2024-05-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0004_missao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missao',
            name='imagem',
            field=models.ImageField(upload_to='imagens'),
        ),
    ]
