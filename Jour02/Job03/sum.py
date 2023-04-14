from random import randint

def Sum(number1, number2):
    result = number1 + number2
    print("Résultat : {}".format(result))

i = 0

while i < 10:
    Sum(randint(1, 100), randint(1, 100))
    i += 1