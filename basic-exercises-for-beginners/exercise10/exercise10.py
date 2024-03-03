def lista(*varden):
    resultat = []
    if varden:
        resultat.extend([num for num in varden[0] if num % 2 != 0])

        for varden2 in varden[1:]:
            resultat.extend([num for num in varden2 if num % 2 == 0])
    return resultat


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

resultat = lista(list1, list2)
print(resultat)
