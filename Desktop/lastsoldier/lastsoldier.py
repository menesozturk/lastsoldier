def sonuncuasker(soldiers):#Bu fonksiyon da soldiers değişkininin değerine kadar sayida askerin dairesel ates sonucu son kalan askeri verir.
    askerler = list(range(1, soldiers + 1)) # Asker sayisi uzunlugunda bir list oluşturuluyor.
    while len(askerler) > 1: # Asker listesindeki uzunluktan 1'den fazla oldugu surece islem devam edicek.
        for index, _ in enumerate(askerler):
            del askerler[(index + 1) % len(askerler)] # Her askerin yanindaki askeri listeden silicek.
    return askerler[0] # En son kalan askeri return edicek.

sayi=input("Asker sayısını giriniz --> ") # Asker sayisini kullanıcıdan alıyoruz.
soldiers=int(sayi) # soldiers degiskenini integer türünden bir degişken olarak belirliyoruz.
print("Sağ kurtulan asker --> " + str(sonuncuasker(soldiers)) + ". askerdir.") # soldiers degiskenini sonuncuasker fonksiyonuna yollayıp,ekrana yazıyoruz.
