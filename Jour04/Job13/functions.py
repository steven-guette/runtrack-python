from Class.whiteshield import WShield

def RemoveDuplicatesFromList(anList):
    if WShield.IsList(anList):
        i = 0

        while i < len(anList):
            if anList[i] in anList[i+1:]:
                del anList[i]
            else:
                i += 1