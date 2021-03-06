# Generated by Django 2.1.3 on 2018-11-07 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('seudonimo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('editorial', models.CharField(max_length=60)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unidades', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Libro'),
        ),
        migrations.AddField(
            model_name='autor',
            name='libros',
            field=models.ManyToManyField(through='libros.Clasificacion', to='libros.Libro'),
        ),
    ]
