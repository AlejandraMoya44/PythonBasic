def nums_que_comencen_per(llista, lletra):
    comptador = 0
    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            comptador +=1
    return comptador
def main():
    lletra = input("Introdueix una lletra:")
    llista_noms = ["Anna", "Albert", "Joan", "Arnau", "Maria", "Marta", "Miquel"]
    print(f"Noms que comencen per '{lletra}':")
    nombre_noms ? nums_que_comencen_per(llista_noms, lletra)
    print(nombre_noms)
main()