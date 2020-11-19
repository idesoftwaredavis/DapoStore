# Generated by Django 3.1.2 on 2020-10-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='nombre usuario')),
                ('password', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('security_question', models.CharField(choices=[('¿Cual es tu banda favorita?', 1), ('¿Objeto mas valioso para usted?', 2), ('¿Nombre de su perro?', 3)], default='Elija pregunta', max_length=50, verbose_name='Pregunta Seguridad')),
            ],
        ),
    ]
