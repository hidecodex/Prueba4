# Generated by Django 3.2.1 on 2021-07-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=99)),
                ('Autor', models.CharField(max_length=99)),
                ('Precio', models.IntegerField(default=0)),
                ('Stock', models.IntegerField(default=0)),
                ('Publicacion', models.DateField()),
            ],
        ),
    ]