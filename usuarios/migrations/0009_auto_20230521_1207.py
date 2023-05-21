# Generated by Django 3.2.2 on 2023-05-21 17:07

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20230521_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='departamento', chained_model_field='departamento', default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.ciudad'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='departamento',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='departamento',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
