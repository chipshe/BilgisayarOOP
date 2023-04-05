from function import *

bilgisayar = Bilgisayar()

print_menu()

while True:
    secim = input('Seçiminiz : ')

    if secim == "q":
        print('Program Kapatildi..')
        break
    elif secim == "1":
        bilgisayar.bilgisayarAc()
    elif secim == "2":
        bilgisayar.bilgisayarKapat()
    elif secim == "3":
        bilgisayar.dosyaGoruntule()
    elif secim == "4":
        bilgisayar.kapasiteArttir()
    elif secim == "5":
        ekle = input("Birden fazla dosya ekleyecekseniz eklemek istediğiniz dosyalari ',' ile ayirarak ekleyiniz : ")
        ekleDosya = ekle.split(',')

        for eklenecekler in ekleDosya:
            bilgisayar.dosyaEkle(eklenecekler)
    
    elif secim == "6":
        print(bilgisayar)
    else:
        print('Lütfen geçerli bir seçim yapin..')
        continue
