# Generated by Django 3.2.12 on 2022-03-11 16:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perusahaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=500)),
                ('industri_perusahaan', models.CharField(max_length=500)),
                ('alamat_perusahaan', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pekerja',
            fields=[
                ('id_pekerja', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_pekerja', models.CharField(max_length=500)),
                ('posisi_pekerja', models.CharField(max_length=500)),
                ('masa_kontrak_habis', models.DateField()),
                ('perusahaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.perusahaan')),
            ],
        ),
    ]
