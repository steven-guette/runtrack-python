import string
from functions import TextHasChar

charResearch = "e"

print("Saisissez du texte :")
userInput = input("> ")

if TextHasChar(userInput, charResearch):
    charQuantity = userInput.lower().count(charResearch)

    print("La lettre {} a été trouvée {} fois.".format(charResearch.upper(), charQuantity))
else:
    print("La lettre {} n'a pas été trouvée.".format(charResearch))
