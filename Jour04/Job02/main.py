def DisplayFruit(fruitId):
    fruits = ["pomme", "cerise", "orange"]

    try:
        fruitId = int(fruitId)
    except:
        print("Veuillez insérer un identifiant valide.")
    else:
        if 0 <= fruitId < len(fruits): 
            print(fruits[fruitId].capitalize())
        else:
            print("Aucun fruit à afficher.")

DisplayFruit(1)