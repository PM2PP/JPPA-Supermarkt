# Generated by Django 2.2 on 2018-11-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermarkt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lieferant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('LiefernatenNr', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produkte',
            name='Preis',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='produkte',
            name='Standort',
            field=models.IntegerField(default=0),
        ),
    ]
