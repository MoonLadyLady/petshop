# Generated by Django 4.2.5 on 2023-09-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_categoriapet_reserva_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petshop',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ['id'], 'verbose_name': 'Reserva de Banho', 'verbose_name_plural': 'Reservas de Banhos'},
        ),
        migrations.AlterField(
            model_name='categoriapet',
            name='nome',
            field=models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato'), ('outros', 'Outros')], max_length=10, verbose_name='Categoria do Pet'),
        ),
    ]
