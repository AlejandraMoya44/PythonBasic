def calcular_anys(any_actual, nom, any_naixement):
    return any_actual - any_naixement
def imprimir_dades(any_actual, persones):
    print(f"Any actual {any_actual}")
    print("Nom\t\tData naixement\tAnys que farà aquest any")
    for persona in persones:
        nom, any_naixement = persona
        anys = calcular_anys(any_actual, nom, any_naixement)
        print(f"{nom}\t\t{any_naixement}\t\t{anys}")
any_actual = 2022
persones = [("Pere, 2000", "Maria, 1999", "Anna, 2005", "Joan, 1998")]
imprimir_dades(any_actual, persones)