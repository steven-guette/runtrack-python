from classes.whiteshield import WShield

def GetUserInputs():
    stepsNumber = input("Combien de marche y a t'il dans le phare ? ")
    stepsHeight = input("Quelle sont leur hauteur ? ")

    return (stepsNumber, stepsHeight)

def DistanceTraveled(stepsNumber, stepHeight):
    if not WShield.IsInt(stepsNumber, 0):        
        print("\nLe paramètre `stepNumber` doit être un entier. [Min: 0].")
    elif not WShield.IsNumeric(stepHeight, 0, 30):
        print("\nLe paramètre `stepHeight` doit être un numéric. [Min: 0][Max: 30]")
    else:
        message = "\nPour {} marches de {} cm, le gardien parcours {} mètres par semaine."
        distance = (stepsNumber * stepHeight * 2 * 5 * 7) / 100

    print(message.format(stepsNumber, stepHeight, round(distance, 2))) 