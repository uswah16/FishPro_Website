from django.contrib import admin

# Register your models here.

from.models import *

class Perikananadmin(admin.ModelAdmin):
    list_display = ['Provinsi','Jenis_Ikan', 'Jenis_Usaha', 'Tahun', 'Volume_Produksi', 'Nilai_Produksi', 'img', 'Detail']
    search_fields = ['Provinsi','Jenis_Ikan', 'Jenis_Usaha', 'Tahun']
    list_filter = ['Jenis_Usaha']
    list_per_page = 6

admin.site.register(Perikanan, Perikananadmin)
admin.site.register(Tempat)

