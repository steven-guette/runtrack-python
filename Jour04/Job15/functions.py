from Class.whiteshield import WShield

def RoundAndSort(anList):
    if WShield.IsList(anList):
        for i in range(len(anList)):
            anList[i] = round(anList[i])

        anList.sort()

            

            