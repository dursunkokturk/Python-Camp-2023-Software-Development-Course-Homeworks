# Baglanti Kurulacak Database i import Etmek Gerekiyor
import _sqlite3

def list():

    # Database Baglantisi Icin Baglanti Kurulacak Database Uzerinden
    # Connect Fonksiyonu Icinde Baglanilacak Database Adini Yaziyoruz
    connection = _sqlite3.connect("chinook")

    # Database Baglantisinin Atandigi Degisken Adi Uzerinden
    # Execute Fonksiyonu Icinde Calistirilacak Database Sorgusunu Yaziyoruz
    cursor = connection.execute("select * from customers")

    # Database Sorgunun Atandigi Degisken Adi Uzerinden
    # Database Icinde Tarama Yapiyoruz
    # Tarama Sonucunu Baska Bir Degiskene Atama Yapiyoruz
    for line in cursor:

        # Database Icinde Yapilan Sorgulama Sonucunu Ekrana Yazdiriyoruz
        print(line[0])
    
    # Database Baglantisini Kapatiyoruz
    connection.close()

list()