# Generated by Django 4.0 on 2021-12-19 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ancienSujet', '0002_document_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancienSujet.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('filiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancienSujet.filiere')),
            ],
        ),
        migrations.AddField(
            model_name='departement',
            name='faculte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancienSujet.faculte'),
        ),
        migrations.AddField(
            model_name='document',
            name='niveau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ancienSujet.niveau'),
        ),
    ]
