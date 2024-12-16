def elements_parells(llista):
    return [llista[i] for i in range(1, len(llista), 2)]
print(elements_parells(["hola", "món", "això", "és", "un", "exemple", "de", "llista" ]))
print(elements_parells(["paraula", "paraula2", "paraula3", "paraula4"]))
print(elements_parells(["únic"]))
print(elements_parells([]))