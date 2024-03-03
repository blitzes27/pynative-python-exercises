"""funktion som kontrollerar om talen i listan är jämnt
delbara med 5"""


def listan(*varden):
    # Printar ut Given lista
    print(f"Given lista: {varden}\n")
    # Här samlas alla jämnt delbara värden med 5
    resultat = []
    # Forloop för det antal listor som skickas in
    for i in varden:
        # Forloop för alla värden i listan
        for l in i:
            z = l / 5
            # Kontrollerar om resten av z delat med 1
            # är lika med noll. Bara heltal blir lika med noll
            if z % 1 == 0:
                # Lägger till värdet i vårt slut resultat
                resultat.append(l)
    return resultat


g1 = [10, 20, 33, 46, 55]
g2 = [10, 400, 15, 45, 20]

resultat = listan(g1, g2)
print(f"Tal jämnt delbara med 5 är {resultat}\n")
