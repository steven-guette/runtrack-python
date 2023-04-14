def GetValuesToCalculate(numbers):
    values = list()

    if type(numbers) == list and len(numbers) > 0:
        for number in numbers:
            try:
                number = int(number)
            except:
                continue
            else:
                if 25 <= number <= 90:
                    values.append(number)

    return values 

def GetProduct(numbers):
    valuesToMultiply = GetValuesToCalculate(numbers)
    numberOfValues = len(valuesToMultiply)
    finalResult = 0

    if numberOfValues > 0:
        if numberOfValues == 1:
            finalResult = valuesToMultiply[0]
        else:
            for value in valuesToMultiply:
                finalResult *= value

    return finalResult