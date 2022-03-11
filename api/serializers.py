from dataclasses import field
from rest_framework import serializers
from .models import Perusahaan, Pekerja

class PekerjaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Pekerja
        fields = '__all__'

class PerusahaanCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perusahaan
        fields = '__all__'

class PerusahaanSerializer(serializers.ModelSerializer):
     pekerja = PekerjaSerializer(many = True)
     class Meta:
          model = Perusahaan
          fields = ('id', 'nama_perusahaan', 'industri_perusahaan', 'alamat_perusahaan', 'pekerja')