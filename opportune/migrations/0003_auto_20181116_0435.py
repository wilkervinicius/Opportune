# Generated by Django 2.1.3 on 2018-11-16 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opportune', '0002_leadacoes_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadacoes',
            name='data_agenda',
            field=models.DateField(blank=True, null=True, verbose_name='Data Agendamento'),
        ),
        migrations.AddField(
            model_name='leadacoes',
            name='hora_agenda',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Agendamento'),
        ),
        migrations.AddField(
            model_name='leadacoes',
            name='termometro',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='opportune.Termometro'),
        ),
    ]
