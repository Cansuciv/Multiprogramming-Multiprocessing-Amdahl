from multiprocessing import Process
import threading
import time


def karekok_hesapla(sayi):
    karekok = round(sayi**0.5, 2)
    print("Process ID:" + str(threading.get_ident()) + " - Sayi: " + str(sayi) + " - Karekökü: " + str(karekok))
    time.sleep(3)  # Simüle edilen işlem süresi

# Multiprogramming
def coklu_programlama():
    sayilar = [4, 9, 18, 28, 102, 76, 55,102,405]
    print("Çoklu Programlama Başladı.")
    liste1 = []  # Hatalı liste adı düzeltilmiş
    for i in sayilar:
        islem1 = threading.Thread(target=karekok_hesapla, args=(i,))
        liste1.append(islem1)
        islem1.start()

    for islem1 in liste1:
        islem1.join()
        
    print("Çoklu Programlama Tamamlandı!!!")


# Multiprocessing
def coklu_islemci():
    sayilar = [4, 2, 15, 46, 19]
    print("\n\nÇoklu İşlemci Başladı.")
    liste2 = []
    for i in sayilar:
        islem2 = Process(target=karekok_hesapla, args=(i,))  # Burada fonksiyon adı tutarlı oldu
        liste2.append(islem2)
        islem2.start()

    for islem2 in liste2:
        islem2.join()

    print("Çoklu İşlemci Tamamlandı!")

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()
