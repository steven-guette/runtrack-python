def calcule(number1, operator, number2):
    if number2 == 0 and (operator == "/" or operator == "%"):
        return "Il est impossible de diviser par zéro."

    if operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "-":
        return number1 - number2
    elif operator == "%":
        return number1 % number2
    elif operator == "+":
        return number1 + number2
    
def GetUserNumber(inputText):
    number = input("\n" + inputText)

    try:
        number = float(number)
    except:
        print("Veuillez saisir un nombre valide.")
        return GetUserNumber(inputText)
    else:
        return number
    
def GetUserOperator():
    operatorsList = ("+","-", "/", "*", "%")

    print("\nOpérateurs disponibles : + - / * % ")
    operator = input("Saisissez l'opérateur logique de votre choix : ")

    if (operator in operatorsList):
        return operator
    else:
        print("Veuillez saisir un opérateur valide.")
        return GetUserOperator()