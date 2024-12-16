"""
Definir una funció nums_que_comencen_per() que donat una llista de noms,
ens digui quants comencen per la lletra a.
"""


def llegir_llista():
   l=[]
   a="a"
   while a!=".":
       a=input("Introdueix un número: ")
       if a!=".":
           l.append(int(a))
   return l


def noms_que_comencen_per(l,c):
   m=[]
   for e in l:
       senar = len(e)%2==1
       if senar:
           aux=len(e)//2
           if e [aux]==c.upper() or e[aux]==c.lower():
               m.append(e)
       else:
           aux = len(e)//2 -1
           if e [aux]==c.upper() or e[aux]==c.lower() or e[aux+1]==c.upper() or e[aux+1]==c.lower():
               m.append(e)
   print("Els elements de la llista {} que comencen per {} són: {}".format(l,c,m))




#Programa principal
l = llegir_llista()
c = input("Introdueix un caràcter: ")
nom_que_comencen_per(l,c)