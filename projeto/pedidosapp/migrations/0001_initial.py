# Generated by Django 3.2.9 on 2021-11-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pedido', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('valor_pedido', models.CharField(max_length=200)),
                ('endere_pedido', models.CharField(max_length=200)),
            ],
        ),
    ]
