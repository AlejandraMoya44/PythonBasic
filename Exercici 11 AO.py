def comprova_edat(edat):
    if edat < 18:
        return "No és major d'edat."
    elif edat == 18:
        return "Té exactament 18 anys."
    else:
        return "És major d'edat."
def principal():
    try:
        edat = int(input("Introdueix la teva edat:"))
        resultat = comprova_edat(edat)
        print(resultat)
    except valueError:
        print("Si us plau, introdueix un número vàlid.")
if __name__ == "__main__":
    principal()