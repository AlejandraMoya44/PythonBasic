def menu():
   op=0
   # while op <1 and op>5:
   print("Menu")
   print("1. Sumar")
   print("2. Restar")
   print("3. Multiplicar")
   print("4. Dividir")
   print("5. Sortir")
   op= int(input("Introdueixi una opció:"))
   return op
def sumar():
   a = int(input("Introdueixi el primer element"))
   b = int(input("Introdueixi el segon element"))
   c = a + b
   print("El resultat de sumar {} més {} és {}".format (a,b,c))
def restar():
   a =int(input("Introdueixi el primer element"))
   b =int(input("Introdueixi el primer element"))
   c = a - b
   print("El resultat de restar {} menys {} és {}".format (a,b,c))
   def multiplicar():
       a = int(input("Introdueixi el primer element"))
       b = int(input("Introdueixi el segon element"))
       c = a * b
       print("El resultat de multiplicar {} per {} és {}".format(a,b,c))
def dividir():
   a = int(input("Introdueixi el primer element"))
   b = int(input ("Introdueixi el primer element"))
   c = a / b
   print("El resultat de dividir {} entre {} és {}".format(a,b,c))
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
           a= False
           print("Adéu, gràcies per haver utilitzar el programa! \n")
       case _:
           print("Opció no vàldia \n")        