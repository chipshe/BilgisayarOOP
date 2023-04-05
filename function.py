import time

def print_menu():
    print("""
    Bilgisayar Uygulamasi
    
        Lütfen Seçim Yapin

            1- Bilgisayari Aç
            
            2- Bilgisayari Kapat

            3- Bilgisayardaki Dosyalari Görüntüle

            4- Kapasiteyi Arttir

            5- Dosya Ekle

            6- Bilgisayarin Güncel Durumu
        
        Çikmak için 'q' ya basin..
""")

class Bilgisayar():
    def __init__(self, bilgisayarDurum = 'Kapali', dosyalar = ['Bilgisayarim','Çöp Kutusu','Google'], kapasite = 250):
        self.bilgisayarDurum = bilgisayarDurum
        self.dosyalar = dosyalar
        self.kapasite = kapasite

    def bilgisayarAc(self):
        if self.bilgisayarDurum == "Acik":
            print("Bilgisayar zaten acik ",self.bilgisayarDurum)
        else:
            print("Bilgisayar Aciliyor..")
            time.sleep(2)
            self.bilgisayarDurum = "Acik"
            print("Bilgisayar Acildi!",self.bilgisayarDurum,"\n")
    
    def bilgisayarKapat(self):
        if self.bilgisayarDurum == "Kapali":
            print("Bilgisayar zaten Kapali ",self.bilgisayarDurum)
        else:
            print("Bilgisayar Kapaniyor..")
            time.sleep(2)
            self.bilgisayarDurum = "Kapali"
            print("Bilgisayar Kapandi!",self.bilgisayarDurum,"\n")
    
    def dosyaEkle(self,ekle):
        if self.bilgisayarDurum == "Kapali":
            print("Lütfen önce bilgisayari açin..")
        else:
            print("Dosya ekleniyor..")
            time.sleep(1)
            self.dosyalar.append(ekle)
            print("Dosya Eklendi!",ekle)
        print("\n")
    
    def dosyaGoruntule(self):
        print("\nMasaüstünde Bulunan Dosyalar")

        tumDosya = self.dosyalar

        for dosya in tumDosya:
            print(f"-> {dosya}")
        print(f"Toplam Dosya Sayisi : {len(self.dosyalar)}\n")

    def kapasiteArttir(self):
        if self.bilgisayarDurum == "Kapali":
            print("Lütfen önce bilgisayari açin..")
        else:
            print(f"Güncel Kapasite : {self.kapasite}GB")
            
            while True:

                try:
                    a = int(input("Bilgisayarin kapasitesini ne kadar arttirmak istiyorsunuz? :"))
                except ValueError:
                    print("Geçersiz Terim Lütfen Tekrar Girin")
                    continue

                print("Kapasite arttiliyor\n")
                time.sleep(2)
                
                self.kapasite += a

                print(f"Başarili bir şekilde kapatise arttirildi!\nGüncel kapasite : {self.kapasite}GB")
                break

    def __str__(self):
        return f"\nBilgisayarin Güncel Durumu\n\nBilgisayar : {self.bilgisayarDurum}\nDosyalar : {self.dosyalar}\nKapasite : {self.kapasite}GB\n"
    
    def __len__(self):
        return len(self.dosyalar)

