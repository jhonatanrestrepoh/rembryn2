# Generated by Django 3.2.2 on 2023-05-22 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_rename_celular_empleado_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='telefono',
            new_name='celular',
        ),
    ]