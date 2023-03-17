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





# Bir Class Icinde, Baska Bir Class Icindeki Fonksiyonlari Ve Ozellikleri Kullanmak Icin
# Ozelliklerin Kullanilacagi Class Icinde, Class Satirinda Parantez Icinde Ozelliklerin
# Alinacagi Class Adini Yaziyoruz
# Bu Isleme inheritance (Miras) Denir
# Bir Class Sadece Bir Class tan inheritance Alabilir
class Statistics(Mathematic):
    def __init__(self) -> None:
        pass
    def varyansCalculate(self):
        return self.s1 + self.s2

statistics = Statistics(5,8)

statistics.total()
statistics.minus()
statistics.multilication()
statistics.division()
statistics.varyansCalculate()