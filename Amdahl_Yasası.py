def hizlanma_hesaplama(paralel_islem, islemci_sayisi):
    if paralel_islem < 0 or paralel_islem > 1:
        raise ValueError("Paralel kısmın oranı 0 ile 1 arasında olmalıdır.") 
    hizlanma = 1 / ((1 - paralel_islem) + (paralel_islem / islemci_sayisi))
    return hizlanma



paralel_islem = float(input("Paralelleştirilebilen kısmın oranını girin (0 ile 1 arasında): "))
islemci_sayisi = int(input("Kullanılacak işlemci sayısını girin: "))

hizlanma_orani = hizlanma_hesaplama(paralel_islem, islemci_sayisi)
print("Paralel işlemle elde edilen hızlanma oranı:" + str(hizlanma_orani))
