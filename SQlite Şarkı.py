import sqlite3
import sys
sys.setrecursionlimit(3000)

c = ""
con = sqlite3.connect("Şarkı.db")
cursor = con.cursor()
def tablo_olustur():
 cursor.execute("CREATE TABLE IF NOT EXISTS şarkıcı (Şarkı_ismi TEXT,Sanatçı TEXT,Albüm TEXT,Prodüksiyon_Şirketi TEXT,Şarkı_süresi INT)")
 con.commit()
tablo_olustur()
con.close
def şarkı_süresi1():
 x = 0
 cursor.execute("Select Şarkı_süresi From şarkıcı  ")
 liste = cursor.fetchall()
 for i in liste:
   i = list(i)
   for a in i:
    x = x + a
   con.commit()
 print("Toplam süre =" + str(x))
def şarkı_ekle():
  Şarkı_ismi = input("Şarkı ismi giriniz:")
  Sanatçı = input ("Sanatçı ismi giriniz:")
  Albüm = input("Albüm ismi giriniz:")
  Prodüksiyon_Şirketi = input("Prodüksüyon şirketi giriniz:")
  Şarkı_süresi = input ("Şarkı süresini saniye cinsinden giriniz:")
  cursor.execute("Insert into şarkıcı Values(?,?,?,?,?)",(Şarkı_ismi,Sanatçı,Albüm,Prodüksiyon_Şirketi,Şarkı_süresi))
  print("Şarkı başarıyla eklendi!!...")
  con.commit()
def şarkı_sil(Şarkı_ismi):
  cursor.execute("Delete from şarkıcı where Şarkı_ismi = ?",(Şarkı_ismi,))
  con.commit()
c = input("Şarkı  eklemek için ekle, silmek için sil, süreler için süre yazınız: ")
if c == "ekle":
 şarkı_ekle()
elif c == "sil":
 a = input("Silinecek şarkının adını giriniz")
 şarkı_sil(a)
 print("Şarkı başarıyla silindi!....")
elif c == "süre":
 şarkı_süresi1()