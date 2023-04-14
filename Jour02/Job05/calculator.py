import os
import functions

playAgain = True

while playAgain:
    firstNumber = functions.GetUserNumber("Indiquez un premier nombre : ")
    secondNumber = functions.GetUserNumber("Indiquez un second nombre : ")
    operatorSelected = functions.GetUserOperator()

    result = functions.calcule(firstNumber, operatorSelected, secondNumber)

    if type(result) == float:
        resultMessage = "\nLe résultat de l'opération ( {} {} {} ) est : {}"
        print(resultMessage.format(firstNumber, operatorSelected, secondNumber, result))
    else:
        print(result)
        
    userContinue = input("\nSouhaitez vous continuer ? ")

    if userContinue.lower() == "non":        
        os.system("cls")
        print("Merci d'avoir joué avec moi, à bientôt ! :)")        
        playAgain = False
    else:
        os.system("cls")