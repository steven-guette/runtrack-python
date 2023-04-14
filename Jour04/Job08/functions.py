def GetEvenValues(numbers):
    evenValues = list()

    if type(numbers) == list and len(numbers) > 0:
        for number in numbers:
            try:
                number = int(number)
            except:
                continue
            else:
                if (number % 2) == 0:
                    evenValues.append(number)
            
    return evenValues

def AddEvenNumbersInList(numbers):
    finalResult = 0

    evenValues = GetEvenValues(numbers)
    evenValuesSize = len(evenValues)

    if evenValuesSize > 0:
        if evenValuesSize == 1:
            finalResult = evenValues[0]
        else:
            finalResult = sum(evenValues)

    print(f"\nRésultat de la somme des valeurs paires : {finalResult}")