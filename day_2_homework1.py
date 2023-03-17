# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. 
# Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

##     Aldığı isim soy isim ile listeye öğrenci ekleyen

##     Listeye birden fazla öğrenci eklemeyi mümkün kılan

##     Listedeki tüm öğrencileri tek tek ekrana yazdıran

##     Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek 
##       öğrencinin numarasını öğrenmeyi mümkün kılan

##     Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

##     Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

## fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

## Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.





# Var Olan List Uzerinden Islemler Yapiyoruz
students = ["Hakan Acar","Mehmet Gencer"]
print("Students List in Ilk Hali")
print(students)
print("")





# List e Her Seferinde 1 Tane Ogreci Ekleme Islemi
def addStudent():
    # Kullanicidan Girdigi Isim Ve Soyisim Bilgisini Aliyoruz
    newStudentFirstNameAndLastName = input("Lutfen Isim ve Soyisim Giriniz : ")

    # Kullanicinin Girdigi Bilgilerin Atandigi Degiskeni Return Ile Dondurerek
    # Islemin Yapimasi Icin Fonksiyonun Cagirilmasi Gerekiyor
    return newStudentFirstNameAndLastName

# AddStudent Fonksiyonu Icinde Dondurelen Degeri Degiskene Atama Yapiyoruz
newStudent = addStudent()

# Fonksiyon Icindeki Dondurelen Degeri
# Fonksiyonun Atandigi Degisken Uzerinden
# Append Fonksiyonu Ile List Icine Ekleme Yapiyoruz 
students.append(newStudent)

# 1 Tane Ogrenci Ekleme Isleminden Sonra List in Guncel Halini Yazdiriyoruz
print(students)
print("")





# List e Tek Seferde Birden Fazla Ogrenci Ekleme Islemi
def multiAddStudent():

    # Kullanicidan List Icinde Eklemek Istedigi Ogrenci Sayisini Aliyoruz
    # Kullanicidan Alinan Deger Sayisal Ancak Veri Tipi String Olduguundan
    # Bu Veri Tipi Ile Islem Yapabilmek Icin Veri Tipini int e Cevirmek Gerekiyor
    addStudentNumber = int(input("Eklemek Istediginiz Ogrenci Sayisini Giriniz : "))

    # Kullanicidan Alinan Degeri Range Fonksiyonu Ile Tarama Islemi Yapiyoruz
    # Tarama Islemi Ile Girilen Sayi Kadar Ogrenci Ismi Girilme Durumunu Kontrol Ediyoruz
    for i in range(addStudentNumber):

        # Kullancidan Alinan Isim Ve Soyisim Bilgisini Degiskene Atama Yapiyoruz
        addMultiStudent = input("Eklemek Istediginiz Ogrenci Adini Ve Soyadini Giriniz : ")

        # Kullanicidan Alinan Isim Ve Soyisim Bilgisinin Atandigi Degisken Icindeki Degeri
        # List Icine Append Fonksiyonu Icinde Parametre Olarak Veriyoruz
        students.append(addMultiStudent)
        print(students)

# Tek Seferde Birden Fazla Ogrenci Ekleme Isleminin Yapilmasi Icin
# Fonksiyonu Cagirmak Gerekiyor
multiAddStudent()

print("")





# List Icindeki Tum Degerleri Yazdiriyoruz
def allStudents(students):    
    for student in students:
        print(student)

print("Tum Ogrenciler")
allStudents(students)

print("")





# List Icindeki Degerlerin indis Numarasi Ogrenci Numarasi Olarak Kabul Ediliyor
def whatIsStudentNumber():

    # Numarasini Ogrenmek Istenilen Ogreci Adini Ve Soyadini Giriyoruz
    studentFirstNameLastName = input("Numarasini Ogrenmek Istediginiz Ogrencinin Adini ve Soyadini Giriniz : ")

    # Adi Ve Soyadi Girilen Ogrencinin Hangi indiste Oldugunu Ogrenmek Icin
    # For Dongusu Icinde Range Fonksiyonunu Kullaniyoruz
    # Range Fonksiyonu Icinde Len Fonksiyonu Ile 
    # List Icindeki Tum indisleri Tek Tek En Sonuna Kadar Geziyoruz
    for i in range(len(students)):

        # Kullanicinin Girdigi Isim Ve Soyisim Bilgisi Ile
        # List Icindeki Degerlerin indis Numaralarini Karsilastiriyoruz
        # Eslesme Olursa Bulunan Degeri Donduruyoruz
        if students[i] == studentFirstNameLastName:
            return i

# Kullanicinin Girdigi Isim Ve Soyisim Bilgisi Ile 
# Eslesen indis Numarasini
# Degiskene Atama Yapiyoruz
studentNumber = whatIsStudentNumber()
print(f"Girdiginiz Ogrencinin Numarasi : {studentNumber}")
print("")





# List Icinde Birden Fazla Ogrenci Silme
def deleteMultiStudent():

    # Kullanici Tarafindan Silinecek Ogrenci Sayisini Aliyoruz
    deleteStudentNumber = int(input("Silmek Istediginiz Ogrenci Sayisini Giriniz : "))
    
    i=0

    # Kullanicinin Girdigi Sayi Kadar Tarama Yapiliyor
    while (i<deleteStudentNumber):

        # Kullanicidan List Icindeki Silinmek Istenilen Isim Ve Soysim Bilgilerini Aliyoruz
        multiFirstNameAndLastName = input("Silmek Istediginiz Ogrencilelerin Adlarini Ve Soyadlarini Tek Tek Giriniz : ")
        
        # Kullanicidan Alinan Isim Ve Soyisim Bilgilerinin Atandigi Degisken Adini
        # List Adi Uzerinden Remove Fonksiyonu Icine Parametre Olarak Veriyoruz
        students.remove(multiFirstNameAndLastName)
        print(students)

        # Birden Fazla Ogrenci Silinmesi Isleminde 
        # Silinmek Istenilen Ogrenci Sayisi Kadar 
        # Isim Girme Islemini Devam Ettiriyoruz
        i+=1
    print(f" Güncel liste: {students}")

# Birden Fazla Ogrenci Silme Isleminin Sonucunu Gormek Icin
# Fonksiyonu Cagirmak Gerekiyor
deleteMultiStudent()