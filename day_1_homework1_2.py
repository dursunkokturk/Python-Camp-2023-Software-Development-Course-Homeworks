# Degisken Olarak Dusundugum Kisimlar

# String Veri Tipi Kurs Adi
courseName = "Yazilim Gelistirici Yetistirme Kampi - Python & Selenium"
print(courseName)
print("")

# Kursun Ilerleme Durumunu Gosteren Bar in Altindaki Sayi
# int Tipinde
# Tamamlandi Yazisi String Tipinde
# Her Iki Veri Birlestirilerek Yazdiriliyor
progressStatus = "% 50"
completionStatus = "Tamamlandi"
print("Kurs Ilerleme Durumu "+ progressStatus +" "+completionStatus)
print("")

# Kursun Yapildigi Tarihini Gosteren Kisim
# DateTime Veri Tipi
datetime = "8 Mart 2023"
print(datetime)
print("")

# String Tipi Veri Olan Onceki Ders Ve Bitir Ve Devam Et Butonlari
previousLecture = "Onceki Ders"
print(previousLecture)
print("")

nextLecture = "Bitir Ve Devam Et"
print(nextLecture)
print("")





# Ders Programı
# Değerlendirme
# Ödev 1
# Ödev 2

# ProgramStatus Degiskenine Atanan Deger
# 0 ise ProgramStatus %25 Seviyesinde Olacak
# 1 ise ProgramStatus %50 Seviyesinde Olacak
# 2 ise ProgramStatus %75 Seviyesinde Olacak
# 3 ise ProgramStatus %100 Seviyesinde Olacak
programStatus = 0
if programStatus == 0:
    print("Ders Programi"+" %25 Tamamlandi.")
elif programStatus == 1:
    print("Degerlendirme"+" %50 Tamamlandi.")
elif programStatus == 2:
    print("Odev1"+" %75 Tamamlandi.")
elif programStatus == 3:
    print("Odev2"+" %100 Tamamlandi.")
else:
    print("Tum Asamalari Basarili Bir Sekilde Bitirdiniz.")
