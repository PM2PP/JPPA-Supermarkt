# Generated by Django 2.2 on 2018-12-12 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supermarkt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sortiment',
            name='Lieferant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Supermarkt.Lieferant'),
            preserve_default=False,
        ),
    ]