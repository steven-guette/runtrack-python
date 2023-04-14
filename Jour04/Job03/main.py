def SetFruits(newFruit):
    fruits = ["pomme", "cerise", "orange"]
    fruits.append(newFruit)

    print("La liste des fruits a été mise à jour :\n{}".format(fruits[:]))

SetFruits("melon")