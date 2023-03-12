ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]

# 1.Soru
ogrenciler.append("Selim Çakır")
print(ogrenciler)

# 2.Soru
ogrenciler.pop(3)
print(ogrenciler)

# 3.Soru
ogrenciler.extend(["Cengiz Baylan","İsmet Yılmaz"])
print(ogrenciler)

# 4.Soru
for i in range(len(ogrenciler)):
    print(ogrenciler[i])

# 5.Soru
print(ogrenciler.index("Kemal Ünlü"))
print(ogrenciler.index("Tarık Sezgin"))
print(ogrenciler.index("İsmail Keskin"))
print(ogrenciler.index("Esat Albayrak"))
print(ogrenciler.index("Cengiz Baylan"))

# 6 ve 7. Sorular
ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]
i=0
while i<len(ogrenciler):
    i+=1
    print(i)
    print(ogrenciler[i])
    if ogrenciler[i]=="İsmail Keskin":
        ogrenciler.remove("İsmail Keskin")
        print(ogrenciler)
        break

print("******************")



ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]
for ogrenci in ogrenciler:
    ogrenci=ogrenciler.pop()
    print(ogrenci)




