# Generated by Django 4.2.4 on 2023-09-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CelTech', '0009_rename_cliente_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]