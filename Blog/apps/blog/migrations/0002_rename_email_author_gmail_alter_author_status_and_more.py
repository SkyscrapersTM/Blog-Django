# Generated by Django 4.1.2 on 2022-10-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='email',
            new_name='gmail',
        ),
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Author On|Off'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status On|Off'),
        ),
    ]
