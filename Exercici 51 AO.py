Hola món això és un exemple de fitxer amb paraules
def crear_llista_fitxer(nom_fitxer):
    with open(nom_fitxer, 'r') as fitxer:
        contingut = fitxer.read()
        paraules = contingut.split()
    return paraules
nom_fitxer = 'paraules.txt'
llista_paraules = crear_llista_fitxer(nom_fitxer)
print("Llista de paraules:", llista_paraules)