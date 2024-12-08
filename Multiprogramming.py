import time

def program1():
    for i in range(10) :# 0'dan 9'a kadar sayılarla döngü çalıştırıyoruz
        print("Program 1 çalışıyor:", i) 
        time.sleep(1)  # Simüle edilen 1 saniyelik gecikme

def program2():
    for i in range(7): # 0'dan 6'ya kadar sayılarla döngü çalıştırıyoruz
        print("Program 2 çalışıyor:", i)
        time.sleep(0.5)  # Simüle edilen 0.5 saniyelik gecikme


if __name__ == "__main__":  
    import threading  
    
    # İlk programı ayrı bir iş parçacığı (thread) olarak çalıştırıyoruz
    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)
    
   
    thread1.start() # İlk iş parçacığını başlatılması
    thread2.start() # İkinci iş parçacığını başlatılması
    
    thread1.join() # İlk iş parçacığının bitmesinin beklenmesi
    thread2.join() # İkinci iş parçacığının bitmesinin beklenmesi
    
    print("Tüm programlar tamamlandı!")
