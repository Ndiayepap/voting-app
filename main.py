import time


# Choix de cuisson
def choix_cuisson(teme):
    choix = input(f"Votre choix entre (1 et {len(teme)}) : ")
    try:
        choix_int = int(choix)
        if choix_int < 1 or choix_int > len(teme):
            print("Erreur!")
            return choix_cuisson(teme)
    except:
        print("Erreur! Vous devez entré des chiffres")
        return choix_cuisson(teme)
    cle = teme[choix_int-1][0]
    valeur = teme[choix_int-1][1]
    return cle, valeur


cuisson = [
    ("Oeufs à la coque", 2),
    ("Oeufs mollets", 6),
    ("Oeufs durs", 9),
]

# Affichage du menu
print("Cuisson de œufs")
index = 0
for c in (cuisson):
    print(index+1, "-", c[0], ":", c[1], "mn")
    index += 1


cle, valeur = choix_cuisson(cuisson)


duree = valeur*60

# Ce programme de type "minuteur" vous permettra d'afficher en temps réel le temps restant de cuisson.
print(cle, ":", valeur, "mn")
print("cuisson en cours", end="", flush=True)
while True:
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
    
    duree -= 10
    min = duree//60 
    if duree == 0:
        print("")
        print("Cuisson terminée !")
        break

    print("")
    print("temps restant",str(min).zfill(2) + ":" + str(duree-min*60).zfill(2), end="", flush=True)
    





