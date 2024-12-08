from multiprocessing import Process
import os
import time


def bilgilendirme(sayi):
    print("Islemci: " + str(os.getpid()) + " - Sayi: " + str(sayi) + " - Kare: " + str(sayi * sayi))
    time.sleep(0.27)  # Simüle edilen işlem süresi

if __name__ == "__main__":
    print("Multiprocessing  işlemi baslıyor!!!")
    
    sayilar = [2, 12, 7, 28, 49, 3, 34, 45]  # Sayılar değiştirildi
    bilgiler = []
   
    for i in sayilar:
        bilgi = Process(target=bilgilendirme, args=(i,))
        bilgiler.append(bilgi)
        bilgi.start()
        
    # İşlemleri tamamla
    for i in bilgiler:
        i.join()
        
    print("Tüm İşlemler Tamamlandı!")
    

