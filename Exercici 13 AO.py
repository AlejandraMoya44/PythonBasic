def menu():
   print("Menu")
   print("1. Sumar")
   print("2. Restar")
   print("3. Multiplicar")
   print("4. Dividir")
   print("5. Canvi de base")
   print("6. Sortir")
   op= int(input("Introdueixi una opció:"))
   return op
def sumar():
   a = int(input("Introdueixi el primer element"))
   b = int(input("Introdueixi el segon element"))
   c = a + b
   print(f"El resultat de sumar {a} més {b} és {c}")
def restar():
   a =int(input("Introdueixi el primer element:"))
   b =int(input("Introdueixi el primer element:"))
   c = a - b
   print(f"El resultat de restar {a} menys {b} és {c}")
def multiplicar():
       a = int(input("Introdueixi el primer element:"))
       b = int(input("Introdueixi el segon element:"))
       c = a * b
       print(f"El resultat de multiplicar {a} per {b} és {c}".)
def dividir():
   a = int(input("Introdueixi el primer element:"))
   b = int(input ("Introdueixi el primer element:"))
   if b != 0:
       c = a / b
   print(f"El resultat de dividir {a} entre {b} és {c}")
else:
    print("No es pot dividir per zero.")
def canvi_base():
    print("Canvi de base")
    print("1. Decimal a Binari")
    print("2. Decimal a Octal")
    print("3. Decimal a Hexadecimal")
    op_base = int(input("Introdueixi un a opció:"))
    num = int(input("Introdueixi el número decimal: "))
    if op_base == 1:
        print(f"El número {num} en binari és {bin(num)[2:]}")
    elif op_base == 2:
        print(f"El número {num} en octal és {oct(num)[2:]}")
    elif op_base == 3:
        print(f"El número {num} en hexadecimal és {hex(num)[2:]}")
a = True
while a:
   op = menu()
   match op:
       case 1:
           sumar()
       case 2:
           restar()
       case 3:
           multiplicar()
       case 4:
           dividir()
       case 5:
           canvi_base()
       case 6:
           a = False    
           print("Adéu, gràcies per haver utilitzar el programa!\n")
       case _:
           print("Opció no vàldia\n")    