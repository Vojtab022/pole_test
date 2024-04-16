Zboží = ["NVIDIA RTX 3060", "NVIDIA RTX 3060 Ti", "NVIDIA RTX 3070", "NVIDIA RTX 3070 Ti", "NVIDIA RTX 3080", "NVIDIA RTX 3080 Ti", "NVIDIA RTX 3090"]
Košík = []

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f" {x+1}: {prvek[x]}")
        print(" ")
print("")
print("Vítejte v obchodě")
print("")
print("--------------------")
print("")
print("Náše nabídka:")
print("")



while(True):
    vypis_pole(Zboží)
    print("--------------------")
    
    prvek_vyber = (input("Zadejte číslo zboží, které chcete přidat do košíku: "))
        
    if prvek_vyber == "konec":
        print("Děkujeme za nákup")
        break

    else:
        prvek_vyber = int(prvek_vyber) - 1
        if -1<prvek_vyber<len(Zboží):
            
            prvek_vyber2 = Zboží[prvek_vyber]

            Košík.append(prvek_vyber2)

            Zboží.pop(prvek_vyber)

            print("--------------------")
            print("")
            print("Pro dokončení nákupu zadejte konec")
            print("")
            print("--------------------")
            print("")
            print("Obsah košíku:")
            print("")
            vypis_pole(Košík)
            print("")
            print("--------------------")
            print("Naše nabídka:")
            print("")
        
        
        else:
            print("")
            print("Nevybral jsi z nabídky vyber znovu")
            print("")