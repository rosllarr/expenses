# Generated by Django 4.2 on 2023-04-21 09:21

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
                ('reserved_transection_date', models.DateField()),
                ('transection_date', models.DateField(auto_now=True)),
                ('income', models.DecimalField(decimal_places=7, max_digits=7)),
                ('expenses', models.DecimalField(decimal_places=7, max_digits=7)),
            ],
        ),
    ]
