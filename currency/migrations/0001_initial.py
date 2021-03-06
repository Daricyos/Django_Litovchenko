# Generated by Django 3.2.5 on 2021-09-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('RUR', 'Ruble')], max_length=4)),
                ('source', models.CharField(max_length=20)),
                ('buy_price', models.DecimalField(decimal_places=5, max_digits=19)),
                ('sell_price', models.DecimalField(decimal_places=5, max_digits=19)),
            ],
        ),
    ]
