# Generated by Django 4.2 on 2023-04-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('reserved_transection_date', models.DateField(default=None, verbose_name='date reserved')),
                ('transection_date', models.DateField(default=None, verbose_name='action date')),
                ('income', models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='income')),
                ('expenses', models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='expenses')),
                ('reserved_expenses', models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='reserved expenses')),
            ],
        ),
    ]
