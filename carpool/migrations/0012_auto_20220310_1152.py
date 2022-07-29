# Generated by Django 3.2.10 on 2022-03-10 11:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0011_auto_20220308_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='carona',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.CharField(default='/carpool/assets/profiles/man.svg', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensagemusuarios',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='msgdestinatario', to='carpool.usuario'),
        ),
        migrations.AlterField(
            model_name='mensagemusuarios',
            name='remetente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='msgremetente', to='carpool.usuario'),
        ),
    ]