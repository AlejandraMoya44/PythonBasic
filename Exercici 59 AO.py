def es_primer(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
def llista_primers_i_comptar():
    primers = []
    for num in range(1, 101):
        if es_primer(num):
            primers.append(num)
    return primers
primers = llista_primers_i_comptar()
print("Números primers entre 1 i 100:", primers)
print("Total de números primers:", len(primers))