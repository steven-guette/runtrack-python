import functions

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

print(f"La liste utilisée : {L[:]}\n")
print(f"Le nombre le plus élevé est {functions.GetMaxRangeInList(L)}")
print(f"Le nombre le plus bas est {functions.GetMinRangeInList(L)}")