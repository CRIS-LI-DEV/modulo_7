# Generated by Django 4.2.2 on 2023-06-30 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.estado'),
        ),
    ]