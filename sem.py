import os
import sys

print("GNOME Masaustu Kurulum Sihirbazina Hos Geldiniz...")
x = int(input("Lutfen Isleminizi Seciniz\n 1-) GNOME Ortamini kur\n 2-) Cikis : "))


gnome = ('sudo pacman -S gnome')
gnome2 = ('sudo systemctl start gdm.service')
guncelle = ("sudo pacman -Syu")

if x == 1:
    print("\nGnome Ortami Kuruluyor")
    os.system(guncelle)
    os.system(gnome)
    os.system(gnome2)
    print("\nGnome Kuruldu")


elif x == 2:
    print("\nCikis Yapiliyor....")
    sys.exit()
