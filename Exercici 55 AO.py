def suma_entre_dos_numero(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    suma = sum(range(num1, num2 + 1))
    return suma
def main():
    while True:
        try:
            num1 = int(input("Introdueix e primer número: "))
            num2 = int(input("Introdueix el segon número: "))
            break
        except valueError:
            print("Si us plau, introdueix números enters vàlids.")
    resultat = suma_entre_dos_numeros(num1, num2)
    print(f"La suma de tots els números entre {num1} i {num2} és: {resultat}")
main()