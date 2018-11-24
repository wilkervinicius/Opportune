# Generated by Django 2.1.3 on 2018-11-19 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opportune', '0003_auto_20181116_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='data_agenda',
            field=models.DateField(blank=True, null=True, verbose_name='Data Agendamento'),
        ),
        migrations.AddField(
            model_name='lead',
            name='hora_agenda',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Agendamento'),
        ),
        migrations.AlterField(
            model_name='leadacoes',
            name='data_agenda',
            field=models.DateField(blank=True, null=True, verbose_name='Data Contato'),
        ),
        migrations.AlterField(
            model_name='leadacoes',
            name='hora_agenda',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Contato'),
        ),
        migrations.AlterField(
            model_name='leadacoes',
            name='lead',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_acoes', to='opportune.Lead', verbose_name='Lead'),
        ),
        migrations.AlterField(
            model_name='leadacoes',
            name='termometro',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_acoes', to='opportune.Termometro', verbose_name='Termometro'),
        ),
    ]
