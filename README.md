# Eksplorasi Lab 4 Layanan Aplikasi Web: Implementasi CRUD

Dokumentasi Postman: https://documenter.getpostman.com/view/15242408/UVsHUo4U

## URL API (LOCALHOST)
```
URL Localhost: http://127.0.0.1:8000/
URL Create dan Get All Perusahaan (without id): http://127.0.0.1:8000/api/perusahaan
URL Get, Update, Delete by Id Perusahaan: http://127.0.0.1:8000/api/perusahaan/<int:pk>
URL Create dan Get All Pekerja (without id): http://127.0.0.1:8000/api/pekerja
URL Get, Update, Delete by Id Pekerja: http://127.0.0.1:8000/api/pekerja/<str:pk>
```
## Credentials

Tidak perlu makemigrations atau migrate karena saya menyertakan db sqlite dan migrations yang saya pakai di local. Apabila ingin masuk ke django admin untuk membuat atau melihat user baru, saya telah membuat superuser nya yaitu
```
username: admin
password: admin
```
