import includes.functions as func

(stepsNumber, stepHeight) = func.GetUserInputs()

try:
    stepsNumber = int(stepsNumber)
    stepHeight = float(stepHeight)
except:
    print("\nLe nombre de marche et la hauteur des marches doivent êtredes nombres valides.")

func.DistanceTraveled(stepsNumber, stepHeight)