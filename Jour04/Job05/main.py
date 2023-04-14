from random import randint

def GenerateRandIntList(quantity, minValue, maxValue):
    intList = list()

    try:
        quantity = int(quantity)
        minValue = int(minValue)
        maxValue = int(maxValue)
    except:
        print("Les arguments de cette fonction n'acceptent que des valeurs numériques.")
    else:
        if minValue > maxValue:
            print("La valeur de `minValue`est plus grande que celle de `maxValue`.")
        else:
            for i in range(quantity):
                intList.append(randint(minValue, maxValue))
    finally:
        return intList
    
def ReplaceBySum(listToReplace, index):
    listLength = len(listToReplace)

    if listLength > 0:
        try:
            index = int(index)
        except:
            print("L'index doit être une valeur numérique.")
        else:
            if 0 <= index < listLength:
                if (index+1) == listLength:
                    newValue = (listToReplace[index-1] + listToReplace[0])
                else:
                    newValue = (listToReplace[index-1] + listToReplace[index+1])

                listToReplace[index] = newValue
            else:
                print("L'index à remplacer n'existe pas.")

    
L = GenerateRandIntList(10, 1, 100)

print(f"Le contenu de la liste :\n{L[:]}")

print(f"\nLa valeur de l'index 1 :\n{L[1]}")

ReplaceBySum(L, 3)

print(f"\nLe contenu de la liste une fois le quatrième élement remplacé :\n{L[:]}")

print(f"\nLe dernier élement de la liste :\n{L[-1]}")

