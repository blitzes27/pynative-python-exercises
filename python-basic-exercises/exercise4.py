def remove_chars(ord=None, grad=None):
    k = ord[grad:]
    if ord == None or len(ord) < 1 or (isinstance(grad, int) and grad > len(ord)):
        print(
            f'tillräkligt långt ord saknas,\nantal bokstäver är "{len(ord)}" och grad\när "{grad}"går ej att göra uppgift\n'
        )
        return 1, k

    elif grad == None or grad == 0:
        # grad = 0
        print(f'Givet ord är = "{ord}" \nmed grad "{grad}"\nresultatet blir "{ord}"\n')
        return 2, k

    elif ord == None or len(ord) < 1 and grad == None or grad == 0:
        Print("Inget ord eller grad har givits\n")
        return 3, k

    elif len(ord) > 0 or ord != None and grad != None or grad > 0:
        print(
            f'Givet ord = "{ord}"\ngraden är "{grad}"\nresultatet blir "{ord[grad:]}"\n'
        )
        return 1, k


ett = remove_chars("", 0)

två = remove_chars(
    "",
)

tre = remove_chars(
    "pynative",
)

fyra = remove_chars("pynative", 3)
