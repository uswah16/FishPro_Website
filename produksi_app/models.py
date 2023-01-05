from django.db import models

# Create your models here.

class Tempat(models.Model):
    provinsii = models.CharField(max_length=20)
  
    def __str__(self):
        return self.provinsii


class Perikanan(models.Model):
    Jenis_Ikan = models.CharField(max_length=15)
    Jenis_Usaha = models.CharField(max_length=30)
    Tahun = models.IntegerField(null=True)
    Volume_Produksi = models.CharField(max_length=30)
    Nilai_Produksi = models.CharField(max_length=30)
    img = models.CharField(max_length=15, null= True)
    Provinsi = models.ForeignKey(Tempat, on_delete=models.CASCADE, null=True)
    Detail = models.URLField(max_length=100)
    
    def __str__(self):
        return self.Jenis_Ikan

