nev=input("Név: ")
print("Karakterek száma: ",len(nev))
db=0
if('a' in nev) or ('A' in nev):
    for karakter in nev:
        if(karakter=='a') or (karakter=='A'):
            db+=1
    print("Van benne 'a' betű, "+str(db)+" db")
else:
    print("Nincs benne 'a' betű.")


split= nev.split(" ")
print("Vezetéknév: ",split[0])
for nev in split[1:]:
    print("Keresztnév: ",nev)

javitva=[]
for nev in split:
    nagyban=nev[0].upper()+nev[1:]
    javitva.append(nagyban)

print(javitva)
