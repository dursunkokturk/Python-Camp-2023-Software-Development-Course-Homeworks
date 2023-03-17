class Mathematic:

    # Conctructor Blok
    def __init__(self,number1,number2) -> None:
        self.n1 = number1
        self.n2 = number2
        print("Mathematic Class i Basladi (Gecici Bellek Heap te Referans Olustu)")

    def total(self):
        return self.n1 + self.n2
    def minus(self):
        return self.n1 - self.n2
    def multilication(self):
        return self.n1 * self.n2
    def division(self):
        return self.n1 / self.n2

# () Parantez Isareti Konuldugunda 
# Bu Islem Yapidiginda Fonksiyon Class Icinde 
# Yukarida Constructor Kod Blogu Calisiyor
# Bu Kod Blogu Icinde Self Anahtar Kelimesi Oldugundan Dolayi
# Class Icindeki Fonksiyonlarda Islem Yapabilmek Icin 
# Self Anahtar Kelimesini Kullaniyoruz
mathematic = Mathematic(3,5)
result = mathematic.total()
print("Total Result : " + str(result))