telsz=input("Írj be egy telefon számot(+36...): ")

if ("+3630" in telsz):
    print("A megadott telefonszám a Telekom szolgáltatóhoz tartozik")
elif ("+3620" in telsz):
    print("A megadott telefonszám a Yettel szolgáltatóhoz tartozik")
elif ("+3670" in telsz):
    print("A megadott telefonszám a Vodafone szolgáltatóhoz tartozik")
else:
    print("Nincs ilyen magyar szolgáltató")


