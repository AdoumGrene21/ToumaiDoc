# Generated by Django 4.0 on 2021-12-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ancienSujet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancienSujet.type'),
        ),
    ]
