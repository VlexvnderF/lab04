# Generated by Django 4.0.3 on 2022-04-08 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cand', models.CharField(max_length=100)),
                ('ape_cand', models.CharField(max_length=100)),
                ('edad_cand', models.IntegerField(max_length=4)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elecciones.region')),
            ],
        ),
    ]