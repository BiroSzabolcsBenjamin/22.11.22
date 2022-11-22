nev=input("Név: ")
print("Karakterek száma: ",len(nev))
db=0
if('a' in nev) or ('A' in nev):
#    print("Van benne 'a' betű.")
    for karakter in nev:
        if(karakter=='a') or (karakter=='A'):
            db+=1
    print("Van benne 'a' betű, "+str(db)+" db")
else:
    print("Nincs benne 'a' betű.")

#db=0

#for karakter in nev:
#    if(karakter=='a'):
#        db+=1
    
#if('a' in nev):
#    print("'a' karakterek száma: ",db)
