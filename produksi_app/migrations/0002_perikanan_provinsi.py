# Generated by Django 4.1.1 on 2022-10-31 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perikanan',
            name='Provinsi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produksi_app.tempat'),
        ),
    ]