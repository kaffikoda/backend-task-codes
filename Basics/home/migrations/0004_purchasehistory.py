# Generated by Django 3.1.7 on 2021-04-25 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_menudetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('restaurant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_amount', models.FloatField(blank=True, null=True)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'purchase_history',
                'managed': False,
            },
        ),
    ]