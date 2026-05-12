# hesap.py - Temel banka hesabi sinifi

class Hesap:
    """Bir banka hesabini temsil eden temel sinif."""

    def __init__(self, hesap_no, sahip, bakiye=0):
        self.__hesap_no = hesap_no   # private - kapsulleme
        self.__sahip = sahip
        self.__bakiye = bakiye
        self.__islemler = []         # isllem gecmisi

    def get_hesap_no(self):
        return self.__hesap_no

    def get_sahip(self):
        return self.__sahip

    def get_bakiye(self):
        return self.__bakiye

    def para_yatir(self, miktar):
        """Hesaba para yatirir."""
        if miktar <= 0:
            print("Miktar 0'dan buyuk olmali!")
            return False
        self.__bakiye += miktar
        self.__islemler.append(f"Yatirma: +{miktar} TL")
        print(f"Basarili! {miktar} TL yatirildi. Yeni bakiye: {self.__bakiye} TL")
        return True

    def para_cek(self, miktar):
        """Hesaptan para ceker."""
        if miktar <= 0:
            print("Miktar 0'dan buyuk olmali!")
            return False
        if miktar > self.__bakiye:
            print("Yetersiz bakiye!")
            return False
        self.__bakiye -= miktar
        self.__islemler.append(f"Cekim: -{miktar} TL")
        print(f"Basarili! {miktar} TL cekildi. Yeni bakiye: {self.__bakiye} TL")
        return True

    def islem_gecmisi(self):
        """Hesabin islem gecmisini gosterir."""
        if not self.__islemler:
            print("Hic islem yapilmamis.")
            return
        print(f"  Islem gecmisi ({self.__sahip}):")
        for i in self.__islemler:
            print(f"    - {i}")

    def bilgi_goster(self):
        """Hesap bilgilerini ekrana yazdirir."""
        print(f"  [{self.__hesap_no}] {self.__sahip} | Bakiye: {self.__bakiye} TL | Tur: Normal")
