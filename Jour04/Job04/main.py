def SetMyBestFruits(newFruit, ranking):
    fruits = ["pomme", "cerise", "orange", "Melon"]

    try:
        ranking = int(ranking)
    except:
        print("Veuillez insérer un numéro de classement valide.")
    else:
        if ranking < len(fruits):
            fruits.insert(ranking, newFruit)
            print(f"La liste de mes fruits favoris a été mise à jour :\n{fruits[:]}")

SetMyBestFruits("Mangue", 2)
