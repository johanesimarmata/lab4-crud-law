from django.db import models
import uuid

class Perusahaan(models.Model):
     nama_perusahaan = models.CharField(max_length=500)
     industri_perusahaan = models.CharField(max_length=500)
     alamat_perusahaan = models.CharField(max_length=500)

     def __str__(self) -> str:
         return "{} - {}".format(self.nama_perusahaan, self.industri_perusahaan)

class Pekerja(models.Model):
     perusahaan = models.ForeignKey(Perusahaan, on_delete=models.CASCADE, related_name='pekerja')
     id_pekerja = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     nama_pekerja = models.CharField(max_length=500)
     posisi_pekerja = models.CharField(max_length=500)
     masa_kontrak_habis = models.DateField()

     def __str__(self) -> str:
         return "{} ({})".format(self.nama_pekerja, str(self.perusahaan))