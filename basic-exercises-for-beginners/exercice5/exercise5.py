# definerar funktionen listan
def listan(*varden):

    # när funktionen får en lista skriver den ut listan
    if len(varden) > 1:
        print(f"givna listor är: {varden}\n")
    else:
        print(f"given lista är: {varden}\n")
    # här samlas varje resultat true eller false i en lista
    resultat = []
    # foorloop för det antal listor som skickas in
    for i in varden:

        # tilldelar variablerna borjan och slut det första och sista värdet i listan
        borjan = i[0]
        slut = i[-1]

        # jämför det första och sista värdet i listan
        if borjan == slut:
            print(f'början: "{borjan}" är lika med slut: "{slut}"\n')
            resultat.append(True)
        else:
            print(f'början: "{borjan}" är skiljt från slut: "{slut}"\n')
            resultat.append(False)
    return resultat


tal = [10, 20, 30, 40, 10]
tal2 = [10, 400, 15, 45, 20]

resultat = listan(tal, tal2)
print(resultat)
