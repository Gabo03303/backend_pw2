# Generated by Django 4.1.6 on 2023-02-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_categoria_pedidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('resenia', models.CharField(max_length=1000)),
            ],
        ),
    ]