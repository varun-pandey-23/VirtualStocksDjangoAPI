# Generated by Django 3.1.7 on 2021-04-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_api', '0006_portfolios_unrealizedvaluecurrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='Unrealizedvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]