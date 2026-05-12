# banka.py - Tum hesaplari yoneten ana sinif

from hesap import Hesap
from tasarruf_hesabi import TasarrufHesabi

class Banka:
    """Bankayi temsil eden ve tum hesaplari yoneten sinif."""

    def __init__(self, banka_adi):
        self.__banka_adi = banka_adi
        self.__hesaplar = []       # tum hesaplari tutan liste
        self.__sonraki_no = 1001   # ilk hesap numarasi

    def hesap_ac(self, sahip, baslangic_bakiye=0):
        """Normal hesap acar."""
        yeni_hesap = Hesap(self.__sonraki_no, sahip, baslangic_bakiye)
        self.__hesaplar.append(yeni_hesap)
        self.__sonraki_no += 1
        print(f"Hesap acildi! Hesap No: {yeni_hesap.get_hesap_no()} | Sahip: {sahip}")

    def tasarruf_hesabi_ac(self, sahip, baslangic_bakiye=0, faiz=0.05):
        """Tasarruf hesabi acar."""
        yeni_hesap = TasarrufHesabi(self.__sonraki_no, sahip, baslangic_bakiye, faiz)
        self.__hesaplar.append(yeni_hesap)
        self.__sonraki_no += 1
        print(f"Tasarruf hesabi acildi! Hesap No: {yeni_hesap.get_hesap_no()} | Sahip: {sahip}")

    def hesap_sil(self, hesap_no):
        """Hesap numarasina gore hesap siler."""
        hesap = self.__no_ile_bul(hesap_no)
        if hesap:
            self.__hesaplar.remove(hesap)
            print(f"Hesap {hesap_no} silindi.")
        else:
            print(f"Hesap {hesap_no} bulunamadi.")

    def para_yatir(self, hesap_no, miktar):
        """Belirtilen hesaba para yatirir."""
        hesap = self.__no_ile_bul(hesap_no)
        if hesap:
            hesap.para_yatir(miktar)
        else:
            print(f"Hesap {hesap_no} bulunamadi.")

    def para_cek(self, hesap_no, miktar):
        """Belirtilen hesaptan para ceker."""
        hesap = self.__no_ile_bul(hesap_no)
        if hesap:
            hesap.para_cek(miktar)
        else:
            print(f"Hesap {hesap_no} bulunamadi.")

    def transfer_yap(self, gonderen_no, alici_no, miktar):
        """Iki hesap arasinda para transferi yapar."""
        gonderen = self.__no_ile_bul(gonderen_no)
        alici = self.__no_ile_bul(alici_no)
        if not gonderen:
            print(f"Gonderen hesap {gonderen_no} bulunamadi.")
            return
        if not alici:
            print(f"Alici hesap {alici_no} bulunamadi.")
            return
        if gonderen.para_cek(miktar):
            alici.para_yatir(miktar)
            print(f"Transfer tamamlandi: {gonderen_no} -> {alici_no} | {miktar} TL")

    def bakiye_sorgula(self, hesap_no):
        """Hesap bakiyesini gosterir."""
        hesap = self.__no_ile_bul(hesap_no)
        if hesap:
            print(f"Hesap {hesap_no} bakiyesi: {hesap.get_bakiye()} TL")
        else:
            print(f"Hesap {hesap_no} bulunamadi.")

    def islem_gecmisi(self, hesap_no):
        """Hesabin islem gecmisini gosterir."""
        hesap = self.__no_ile_bul(hesap_no)
        if hesap:
            hesap.islem_gecmisi()
        else:
            print(f"Hesap {hesap_no} bulunamadi.")

    def tum_hesaplari_listele(self):
        """Tum hesaplari listeler."""
        if not self.__hesaplar:
            print("Hic hesap yok.")
            return
        print(f"\n{self.__banka_adi} - Toplam {len(self.__hesaplar)} hesap:")
        print("-" * 55)
        for hesap in self.__hesaplar:
            hesap.bilgi_goster()
        print("-" * 55)

    def istatistik(self):
        """Banka istatistiklerini gosterir."""
        toplam = len(self.__hesaplar)
        toplam_bakiye = sum(h.get_bakiye() for h in self.__hesaplar)
        tasarruf = sum(1 for h in self.__hesaplar if isinstance(h, TasarrufHesabi))
        print(f"\nIstatistik:")
        print(f"  Toplam Hesap    : {toplam}")
        print(f"  Tasarruf Hesabi : {tasarruf}")
        print(f"  Normal Hesap    : {toplam - tasarruf}")
        print(f"  Toplam Bakiye   : {toplam_bakiye} TL")

    def __no_ile_bul(self, hesap_no):
        """Private metod: hesap numarasiyla hesap nesnesini dondurur."""
        for hesap in self.__hesaplar:
            if hesap.get_hesap_no() == hesap_no:
                return hesap
        return None
