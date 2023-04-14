from random import randint

IsNotEmpty = lambda anList: (type(anList) == list and len(anList) > 0)

def ReverseEndsList(listToReverse):
    if IsNotEmpty(listToReverse):
        elements = len(listToReverse)

        if elements == 2:
            listToReverse.reverse()
        elif elements > 2:
            listToReverse.insert(0, listToReverse[-1])
            listToReverse[-1] = listToReverse[1]
            del listToReverse[1]

def GenerateIntList(size):
    intList = list()

    try:
        size = int(size)
    except:
        print("Le paramètre saisi doit être une valeur numérique.")
    else:
        for i in range(size):
            intList.append(randint(1, 100))
    finally:
        return intList

myFirstList = GenerateIntList(2)
mySecondList = GenerateIntList(5)

if IsNotEmpty(myFirstList) and IsNotEmpty(mySecondList):

    # Traitement de la première liste
    print(f"Ma première liste :\n{myFirstList}")
    ReverseEndsList(myFirstList)
    print(f"\nMa première liste modifiée :\n{myFirstList}")

    # Traitement de la seconde liste
    print(f"\nMa seconde liste :\n{mySecondList}")
    ReverseEndsList(mySecondList)
    print(f"\nMa seconde liste modifiée :\n{mySecondList}")