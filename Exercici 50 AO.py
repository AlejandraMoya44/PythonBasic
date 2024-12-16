def elimina_duplicats(llista):
    return list(set(llista))
print(elimina_duplicats([1, 2, 3, 4, 4, 5]))
print(elimina_duplicats(["a", "b", "a", "c"]))
print(elimina_duplicats([10, 20, 20, 30, 10]))
print(elimina_duplicats([]))
print(elimina_duplicats([1, 1, 1, 1]))