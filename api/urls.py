from django.urls import path
from .views import PerusahaanView, PekerjaView
app_name = 'api'
urlpatterns = [
     path('perusahaan', PerusahaanView.as_view(), name='perusahaanView'),
     path('perusahaan/<int:pk>', PerusahaanView.as_view(), name='perusahaanViewWithId'),
     path('pekerja', PekerjaView.as_view(), name='pekerjaView'),
     path('pekerja/<str:pk>', PekerjaView.as_view(), name='pekerjaViewWithId'),
]
