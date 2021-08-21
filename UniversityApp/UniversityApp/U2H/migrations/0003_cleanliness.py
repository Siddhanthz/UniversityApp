# Generated by Django 3.1.7 on 2021-04-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('U2H', '0002_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleanliness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.TextField()),
                ('classroom', models.TextField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='U2H.users')),
            ],
        ),
    ]