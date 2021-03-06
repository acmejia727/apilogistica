# Generated by Django 3.2.8 on 2021-10-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iddoc', models.CharField(max_length=100)),
                ('razon_social', models.CharField(max_length=120)),
                ('municipio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
