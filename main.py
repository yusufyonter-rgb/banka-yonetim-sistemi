# main.py - Programin baslangic noktasi

from banka import Banka

def menu_goster():
    """Menuyu ekrana yazdirir."""
    print("\n" + "=" * 42)
    print("        BANKA YONETIM SISTEMI")
    print("=" * 42)
    print("  1 - Normal Hesap Ac")
    print("  2 - Tasarruf Hesabi Ac")
    print("  3 - Hesap Sil")
    print("  4 - Tum Hesaplari Listele")
    print("  5 - Para Yatir")
    print("  6 - Para Cek")
    print("  7 - Transfer Yap")
    print("  8 - Bakiye Sorgula")
    print("  9 - Islem Gecmisi")
    print("  10 - Istatistik")
    print("  0 - Cikis")
    print("=" * 42)

def main():
    """Programin ana dongusu."""
    banka = Banka("Kastamonu Bankasi")

    # Baslangic verileri
    banka.hesap_ac("Ahmet Yilmaz", 5000)
    banka.hesap_ac("Mehmet Kaya", 3000)
    banka.tasarruf_hesabi_ac("Ayse Demir", 10000, 0.08)

    while True:
        menu_goster()
        secim = input("Seciminiz: ").strip()

        if secim == "1":
            sahip = input("Hesap sahibi adi: ")
            bakiye = float(input("Baslangic bakiyesi (TL): "))
            banka.hesap_ac(sahip, bakiye)

        elif secim == "2":
            sahip = input("Hesap sahibi adi: ")
            bakiye = float(input("Baslangic bakiyesi (TL): "))
            faiz = float(input("Faiz orani (ornek 0.05): "))
            banka.tasarruf_hesabi_ac(sahip, bakiye, faiz)

        elif secim == "3":
            no = int(input("Silinecek hesap no: "))
            banka.hesap_sil(no)

        elif secim == "4":
            banka.tum_hesaplari_listele()

        elif secim == "5":
            no = int(input("Hesap no: "))
            miktar = float(input("Yatirilacak miktar (TL): "))
            banka.para_yatir(no, miktar)

        elif secim == "6":
            no = int(input("Hesap no: "))
            miktar = float(input("Cekilecek miktar (TL): "))
            banka.para_cek(no, miktar)

        elif secim == "7":
            gonderen = int(input("Gonderen hesap no: "))
            alici = int(input("Alici hesap no: "))
            miktar = float(input("Transfer miktari (TL): "))
            banka.transfer_yap(gonderen, alici, miktar)

        elif secim == "8":
            no = int(input("Hesap no: "))
            banka.bakiye_sorgula(no)

        elif secim == "9":
            no = int(input("Hesap no: "))
            banka.islem_gecmisi(no)

        elif secim == "10":
            banka.istatistik()

        elif secim == "0":
            print("\nGule gule!")
            break

        else:
            print("Gecersiz secim, tekrar deneyin.")

if __name__ == "__main__":
    main()
