IsListNotEmpty = lambda anList: (type(anList) == list and len(anList) > 0)

def GetMaxRangeInList(numbers):
    highestNumber = 0

    if IsListNotEmpty(numbers):
        for number in numbers:
            if number > highestNumber:
                highestNumber = number

    return highestNumber

def GetMinRangeInList(numbers):
    lowestNumber = GetMaxRangeInList(numbers)

    if IsListNotEmpty(numbers):
        for number in numbers:
            if number < lowestNumber:
                lowestNumber = number

    return lowestNumber