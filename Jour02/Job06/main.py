from random import randint

def Temperature(nombre):
    if nombre > 0:
        outputText = "Positif"
    else:
        outputText = "Négatif"

    print(outputText)

i = 0

while i < 10:
    Temperature(randint(-50, 50))
    i += 1