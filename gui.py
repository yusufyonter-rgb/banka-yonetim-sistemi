# gui.py - Tkinter ile grafik arayuz

import tkinter as tk
from tkinter import messagebox, ttk
from banka import Banka

class BankaGUI:
    """Tkinter kullanarak grafik arayuz olusturan sinif."""

    def __init__(self):
        self.banka = Banka("Kastamonu Bankasi")
        self.banka.hesap_ac("Ahmet Yilmaz", 5000)
        self.banka.hesap_ac("Mehmet Kaya", 3000)
        self.banka.tasarruf_hesabi_ac("Ayse Demir", 10000, 0.08)

        # Ana pencere
        self.pencere = tk.Tk()
        self.pencere.title("Banka Yonetim Sistemi")
        self.pencere.geometry("700x550")
        self.pencere.configure(bg="#1a1a2e")
        self.pencere.resizable(False, False)

        self._arayuz_olustur()

    def _arayuz_olustur(self):
        """Tum arayuz bilesenlerini olusturur."""

        # Baslik
        baslik = tk.Label(self.pencere, text="BANKA YONETIM SISTEMI",
                         font=("Arial", 18, "bold"),
                         bg="#1a1a2e", fg="#e94560")
        baslik.pack(pady=15)

        # Ana cerceve - sol butonlar, sag cikti
        ana_cerceve = tk.Frame(self.pencere, bg="#1a1a2e")
        ana_cerceve.pack(fill="both", expand=True, padx=10)

        # Sol panel - butonlar
        sol = tk.Frame(ana_cerceve, bg="#16213e", width=200)
        sol.pack(side="left", fill="y", padx=(0, 10))
        sol.pack_propagate(False)

        buton_baslik = tk.Label(sol, text="ISLEMLER",
                               font=("Arial", 11, "bold"),
                               bg="#16213e", fg="#e94560")
        buton_baslik.pack(pady=10)

        butonlar = [
            ("Hesap Ac", self.hesap_ac_ekran),
            ("Tasarruf Hesabi Ac", self.tasarruf_ac_ekran),
            ("Para Yatir", self.para_yatir_ekran),
            ("Para Cek", self.para_cek_ekran),
            ("Transfer Yap", self.transfer_ekran),
            ("Bakiye Sorgula", self.bakiye_ekran),
            ("Tum Hesaplar", self.listele),
            ("Istatistik", self.istatistik),
        ]

        for metin, komut in butonlar:
            btn = tk.Button(sol, text=metin, command=komut,
                           bg="#0f3460", fg="white",
                           font=("Arial", 10),
                           relief="flat", cursor="hand2",
                           width=18, pady=6)
            btn.pack(pady=3, padx=10)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#e94560"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#0f3460"))

        # Sag panel - cikti alani
        sag = tk.Frame(ana_cerceve, bg="#16213e")
        sag.pack(side="right", fill="both", expand=True)

        cikti_baslik = tk.Label(sag, text="SONUC",
                               font=("Arial", 11, "bold"),
                               bg="#16213e", fg="#e94560")
        cikti_baslik.pack(pady=10)

        self.cikti = tk.Text(sag, bg="#0d0d0d", fg="#00ff88",
                            font=("Courier", 10),
                            relief="flat", state="disabled",
                            wrap="word")
        self.cikti.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Temizle butonu
        temizle_btn = tk.Button(sag, text="Temizle", command=self.temizle,
                               bg="#e94560", fg="white",
                               font=("Arial", 9), relief="flat", cursor="hand2")
        temizle_btn.pack(pady=(0, 10))

        self.listele()  # Baslangicta hesaplari goster

    def _yaz(self, metin):
        """Cikti alanina yazi yazar."""
        self.cikti.config(state="normal")
        self.cikti.insert("end", metin + "\n")
        self.cikti.config(state="disabled")
        self.cikti.see("end")

    def temizle(self):
        self.cikti.config(state="normal")
        self.cikti.delete("1.0", "end")
        self.cikti.config(state="disabled")

    def listele(self):
        self.temizle()
        hesaplar = self.banka.get_hesaplar()
        self._yaz(f"Toplam {len(hesaplar)} hesap:\n" + "-"*40)
        for h in hesaplar:
            tur = "Tasarruf" if hasattr(h, '_TasarrufHesabi__faiz_orani') else "Normal"
            self._yaz(f"[{h.get_hesap_no()}] {h.get_sahip()} | {h.get_bakiye()} TL | {tur}")

    def istatistik(self):
        self.temizle()
        self.banka.istatistik_yaz(self._yaz)

    def hesap_ac_ekran(self):
        pencere = tk.Toplevel(self.pencere)
        pencere.title("Hesap Ac")
        pencere.geometry("300x200")
        pencere.configure(bg="#1a1a2e")

        tk.Label(pencere, text="Ad Soyad:", bg="#1a1a2e", fg="white").pack(pady=5)
        ad = tk.Entry(pencere, width=25)
        ad.pack()

        tk.Label(pencere, text="Baslangic Bakiyesi:", bg="#1a1a2e", fg="white").pack(pady=5)
        bakiye = tk.Entry(pencere, width=25)
        bakiye.pack()

        def kaydet():
            try:
                self.banka.hesap_ac(ad.get(), float(bakiye.get()))
                self._yaz(f"Hesap acildi: {ad.get()}")
                self.listele()
                pencere.destroy()
            except:
                messagebox.showerror("Hata", "Gecersiz bilgi!")

        tk.Button(pencere, text="Ac", command=kaydet,
                 bg="#e94560", fg="white", relief="flat").pack(pady=15)

    def tasarruf_ac_ekran(self):
        pencere = tk.Toplevel(self.pencere)
        pencere.title("Tasarruf Hesabi Ac")
        pencere.geometry("300x250")
        pencere.configure(bg="#1a1a2e")

        tk.Label(pencere, text="Ad Soyad:", bg="#1a1a2e", fg="white").pack(pady=5)
        ad = tk.Entry(pencere, width=25)
        ad.pack()

        tk.Label(pencere, text="Baslangic Bakiyesi:", bg="#1a1a2e", fg="white").pack(pady=5)
        bakiye = tk.Entry(pencere, width=25)
        bakiye.pack()

        tk.Label(pencere, text="Faiz Orani (ornek: 0.05):", bg="#1a1a2e", fg="white").pack(pady=5)
        faiz = tk.Entry(pencere, width=25)
        faiz.insert(0, "0.05")
        faiz.pack()

        def kaydet():
            try:
                self.banka.tasarruf_hesabi_ac(ad.get(), float(bakiye.get()), float(faiz.get()))
                self._yaz(f"Tasarruf hesabi acildi: {ad.get()}")
                self.listele()
                pencere.destroy()
            except:
                messagebox.showerror("Hata", "Gecersiz bilgi!")

        tk.Button(pencere, text="Ac", command=kaydet,
                 bg="#e94560", fg="white", relief="flat").pack(pady=15)

    def para_yatir_ekran(self):
        self._islem_ekrani("Para Yatir", "Yatir",
                          lambda no, m: self.banka.para_yatir(no, m))

    def para_cek_ekran(self):
        self._islem_ekrani("Para Cek", "Cek",
                          lambda no, m: self.banka.para_cek(no, m))

    def _islem_ekrani(self, baslik, buton, islem):
        pencere = tk.Toplevel(self.pencere)
        pencere.title(baslik)
        pencere.geometry("300x200")
        pencere.configure(bg="#1a1a2e")

        tk.Label(pencere, text="Hesap No:", bg="#1a1a2e", fg="white").pack(pady=5)
        no = tk.Entry(pencere, width=25)
        no.pack()

        tk.Label(pencere, text="Miktar (TL):", bg="#1a1a2e", fg="white").pack(pady=5)
        miktar = tk.Entry(pencere, width=25)
        miktar.pack()

        def kaydet():
            try:
                islem(int(no.get()), float(miktar.get()))
                self.listele()
                pencere.destroy()
            except:
                messagebox.showerror("Hata", "Gecersiz bilgi!")

        tk.Button(pencere, text=buton, command=kaydet,
                 bg="#e94560", fg="white", relief="flat").pack(pady=15)

    def transfer_ekran(self):
        pencere = tk.Toplevel(self.pencere)
        pencere.title("Transfer Yap")
        pencere.geometry("300x250")
        pencere.configure(bg="#1a1a2e")

        tk.Label(pencere, text="Gonderen Hesap No:", bg="#1a1a2e", fg="white").pack(pady=5)
        gonderen = tk.Entry(pencere, width=25)
        gonderen.pack()

        tk.Label(pencere, text="Alici Hesap No:", bg="#1a1a2e", fg="white").pack(pady=5)
        alici = tk.Entry(pencere, width=25)
        alici.pack()

        tk.Label(pencere, text="Miktar (TL):", bg="#1a1a2e", fg="white").pack(pady=5)
        miktar = tk.Entry(pencere, width=25)
        miktar.pack()

        def kaydet():
            try:
                self.banka.transfer_yap(int(gonderen.get()), int(alici.get()), float(miktar.get()))
                self.listele()
                pencere.destroy()
            except:
                messagebox.showerror("Hata", "Gecersiz bilgi!")

        tk.Button(pencere, text="Transfer", command=kaydet,
                 bg="#e94560", fg="white", relief="flat").pack(pady=15)

    def bakiye_ekran(self):
        pencere = tk.Toplevel(self.pencere)
        pencere.title("Bakiye Sorgula")
        pencere.geometry("300x150")
        pencere.configure(bg="#1a1a2e")

        tk.Label(pencere, text="Hesap No:", bg="#1a1a2e", fg="white").pack(pady=10)
        no = tk.Entry(pencere, width=25)
        no.pack()

        def sorgula():
            try:
                hesap = self.banka._Banka__no_ile_bul(int(no.get()))
                if hesap:
                    self._yaz(f"Hesap {no.get()} bakiyesi: {hesap.get_bakiye()} TL")
                else:
                    self._yaz("Hesap bulunamadi!")
                pencere.destroy()
            except:
                messagebox.showerror("Hata", "Gecersiz hesap no!")

        tk.Button(pencere, text="Sorgula", command=sorgula,
                 bg="#e94560", fg="white", relief="flat").pack(pady=15)

    def baslat(self):
        self.pencere.mainloop()
