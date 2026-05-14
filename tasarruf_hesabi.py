# tasarruf_hesabi.py - Hesap sinifından kalitim alan TasarrufHesabi

from hesap import Hesap

class TasarrufHesabi(Hesap):
    """Hesap sinifından turetilen faizli tasarruf hesabi. (Kalitim ornegi)"""

    def __init__(self, hesap_no, sahip, bakiye=0, faiz_orani=0.05):
        super().__init__(hesap_no, sahip, bakiye)  # ust sinif cagrilir
        self.__faiz_orani = faiz_orani  # yillik faiz orani

    def faiz_uygula(self):
        """Hesaba faiz uygular."""
        faiz = self.get_bakiye() * self.__faiz_orani
        self.para_yatir(faiz)
        print(f"  Faiz orani: %{self.__faiz_orani * 100}")

    def bilgi_goster(self):
        """Ust sinifin metodunu override eder, faiz bilgisi ekler."""
        print(f"  [{self.get_hesap_no()}] {self.get_sahip()} | Bakiye: {self.get_bakiye()} TL | Tur: Tasarruf | Faiz: %{self.__faiz_orani * 100}")
