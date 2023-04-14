import functions

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

evenValues = ""

for number in functions.GetEvenValues(L):
    evenValues += f"{number}, "

print(f"La liste utilisée : {L[:]}\n")

if len(evenValues) > 0:
    print("Les valeurs paires présentes dans la liste sont :")
    print(f"{evenValues[0:len(evenValues)-2:]}")
else:
    print("La liste ne contient aucune valeur paire.")

functions.AddEvenNumbersInList(L)
