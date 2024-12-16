def index_paraula(llista, paraula):
    try:
        return llista.index(paraula)
    except ValueError:
        return -1
llista_paraules = ["això", "anem", "exemple", "fitxer", "hola,", "món", "paraules"]
print(index_paraula(llista_paraules, "hola"))
print(index_paraula(llista_paraules, "això"))
print(index_paraula(llista_paraules, "paraula"))
print(index_paraula(llista_paraules, "món"))
print(index_paraula(llista_paraules, "exemple"))