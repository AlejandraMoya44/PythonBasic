def comprovar_rima(paraula1, paraula2):
    if paraula1[-3:] == paraula2 [-3:]:
        return "Rimen"
    elif paraula1[-2:] == paraula2[-2:]:
        return "rimen un poc"
def main():
    paraula1 = input("Introdueix la primera paraula:")
    paraula2 = input("Introdueix la segona paraula:")
    resultat = comprovar_rima(paraula1, paraula2)
    print(resultat)
main()