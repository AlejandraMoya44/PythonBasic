def llegir_llista():
   a = l[]
   a="a"
   while a!=".":
       a=input("Introdueix una paraula: ")
       if a!=".":
           l.append(a)
   return l
def paraula_de_cada_longitud(l):
   a = []
   for e in l:
       a.append(len(e))
   b = set(a)
   for e in b:
       y = len(list(filter(lambda x:x==e,a)))
       c.append([e,y])
   return c


#Programa principal
a = llegir_llista()
print("La paraula més llarga de la llista {} és {}".format(a,paraula<_mes_llarga(a)))