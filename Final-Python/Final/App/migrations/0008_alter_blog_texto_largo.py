# Generated by Django 4.1 on 2022-09-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_blog_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='texto_largo',
            field=models.TextField(),
        ),
    ]
