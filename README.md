# Banka Yonetim Sistemi

Python ile OOP kullanarak gelistirilmis konsol tabanli banka yonetim sistemi.

## Dosyalar
- main.py - Programin baslangic noktasi, menu dongusu
- banka.py - Tum hesaplari yoneten Banka sinifi
- hesap.py - Temel Hesap sinifi (kapsulleme)
- tasarruf_hesabi.py - Hesap sinifından turetilen TasarrufHesabi (kalitim)

## Nasil Calistirilir
1. Python 3.x yukleyin
2. 4 dosyayi ayni klasore koyun
3. main.py dosyasini calistirin

## Kullanilan Teknolojiler
- Python 3.x
- OOP: Kapsulleme, Kalitim, Cok Bicimlilik

## Proje Ozellikleri
- Normal ve tasarruf hesabi acilab ilir
- Para yatirma ve cekme islemi yapilabilir
- Iki hesap arasinda transfer yapilabilir
- Bakiye sorgulanabilir
- Islem gecmisi goruntulenebilir
- Tum hesaplar listelenebilir
- Banka istatistikleri goruntulenebilir

## Kullanilan OOP Kavramlari
- Kapsulleme: hesap.py dosyasinda tum degiskenler __ ile private tanimlandi
- Kalitim: TasarrufHesabi sinifi, Hesap sinifından turetildi
- Cok Bicimlilik: bilgi_goster metodu TasarrufHesabi sinifinda override edildi
- Soyutlama: __no_ile_bul metodu private olarak tanimlandi
