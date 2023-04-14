from Class.whiteshield import WShield

def IncrementElementsOfList(anList):
    if WShield.IsList(anList):
        for i in range(len(anList)):
            if WShield.IsNumeric(anList[i]):
                anList[i] += 1    