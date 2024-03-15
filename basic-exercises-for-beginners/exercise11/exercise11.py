def rewind_space(*varde):
    for tal in varde:
        resultat = tal[::-1]
        resultat1 = list(resultat)
        print(*resultat1, sep=" ")


g1 = rewind_space("45678")
g2 = rewind_space("12345678")
