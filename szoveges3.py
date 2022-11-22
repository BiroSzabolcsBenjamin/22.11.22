telsz=input("Írj be egy telefon számot: ")

if (telsz[3:5]=="30"):
    print("A megadott telefonszám a Telekom szolgáltatóhoz tartozik")
elif (telsz[3:5]=="20"):
    print("A megadott telefonszám a Yettel szolgáltatóhoz tartozik")
elif (telsz[3:5]=="70"):
    print("A megadott telefonszám a Vodafone szolgáltatóhoz tartozik")
else:
    print("Nincs ilyen magyar szolgáltató")


