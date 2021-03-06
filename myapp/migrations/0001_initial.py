# Generated by Django 3.2.6 on 2021-09-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('countrycode', models.CharField(max_length=4)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
