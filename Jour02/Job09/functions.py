import math

def IsRectangle(a, b , c):
    hypotenuse = 0
    others = 0

    for lenght in (a, b, c):
        others += math.pow(lenght, 2)

        if lenght > hypotenuse:
            hypotenuse = lenght

    hypotenuse = math.pow(hypotenuse, 2)
    others -= hypotenuse

    return (round(hypotenuse) == round(others))

def IsIsocele(a, b, c):
    return (a == b or a == c or b == c)
    
def IsEquilateral(a, b, c):
    return (a == b == c)

    
    