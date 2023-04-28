# Generated by Django 4.2 on 2023-04-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inex', '0003_alter_expenses_expenses_alter_expenses_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expenses',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='expenses'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='income',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='income'),
        ),
    ]