# Generated by Django 4.1 on 2022-08-22 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announ',
            name='type_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announ.annountype'),
        ),
    ]
