Python Data Types (Python Veri Tipleri)

Önce Genel Olarak Veri Tiplerini Görelim. Sonra Detaylarına Bakalım

String (Text)

String

Char

Numerik (Sayısal)

int

Long

Float

Double

Complex

Boolean

Sequence (Sıralama)

List

Tuple

Mapping (Haritalama)

Dictionary

Mapping
Şimdi Sıra Geldi Detaylara Bakmaya
String

En az 2 harften oluşan değerlerin tutulduğu yapılardır.

Örnek değişken tanımlama

b = “book”

Char

Tek bir harften oluşan değerlerin tutulduğu yapılardır.

b = “b”

int

32 bittir. Tam sayı veri tiplerini barındırır.

i = 52434

Long

64 bittir. 12 ve daha fazla haneden oluşan tam sayı veri tiplerini barındırır.

l = 64532646245

Float

Ondalıklı sayılardan oluşan veri tiplerini barındırır.

f = 5.5

Double

Ondalıklı sayı veri tiplerini barındırır.

d = 5.5

Complex

Karmaşık sayısal işlemlerde kullanılır.

Boolean

Yapılan işlemde işlem sonucunun False ( 0 ) yada True ( 1 ) olması durumuna göre yapılacak işleme yön verildiği durumlarda kullanılır.

print( 1 == 1) -> İşlem Sonucu True

print( 1 > 2 ) -> İşlem Sonucu False
Sequence (Sıralama)

Python diline özel olarak oluşan bu veri tipinde list ve tuple gibi alt veri türleri bulunmaktadır. �

    List: Java’da Collection yapılarını incelerken sıklıkla kullanılan List kavramı Python’da bileşik veri tiplerinin bir arada toplanarak çok yönlü işlemlere imkan vermesi sonucu oluşur. İçerisindeki veriler virgülle ayrılır ve köşeli parantez kullanılarak tanımlanır. Veri ekleme işleminden sonra eklenen veriye müdahale edilebilir
    Tuple: Tuple yapı olarak List yapısına oldukça benzer bir veri türüdür. Diğer programlama dillerinde yer alan klasik dizi yapıları gibidir. Liste yapılarından farklı olarak parantez kullanılarak tanımlanır. Veri ekleme işleminden sonra veri üzerinden değişiklik yapılamaz.

Mapping (Haritalama)

Java’da yer alan Collection yapılarının “Map” kavramına oldukça fazla benzeyen Mapping veri tipi içerisinde karma tablo yapıları bulunmaktadır. İçerisindeki yer alan verileri, anahtar ve bu anahtarın karşılığına gelen değerler olarak tutar. Python üzerinde Dictionary olarak bilinen bu veri tipinde tanımlamalar küme parantez kullanılarak ve değer atamaları köşeli parantezler ile gerçekleştirilir.

İsterseniz basit bir Dictionary tanımlayarak içerisine bazı verilerin eklenmesini gerçekleştirelim. Böylelikle Mapping veri tipini daha yakından tanımış oluruz.
