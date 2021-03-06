# Generated by Django 3.1.7 on 2021-04-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_restaurantdetail_resttimingss'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDetails',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('menu_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu_details',
                'managed': False,
            },
        ),
    ]
