# Generated by Django 3.2.2 on 2023-05-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]