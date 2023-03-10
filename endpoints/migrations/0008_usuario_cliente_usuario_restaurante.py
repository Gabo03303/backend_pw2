# Generated by Django 4.1.6 on 2023-03-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0007_pedidos_plato_alter_pedidos_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
