# Generated by Django 3.2.4 on 2021-06-19 12:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, upload_to='photos/customers')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('balance', models.FloatField(default=1000.0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('rec', models.CharField(blank=True, max_length=70)),
                ('amount', models.FloatField()),
                ('send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
