import functions
import math

def Triangles(a, b, c):
    if functions.IsEquilateral(a, b, c):
        type = "équilatéral"
    elif functions.IsRectangle(a, b, c):
        if functions.IsIsocele(a, b, c):
            type = "rectangle isocèle"
        else:
            type = "rectangle"
    elif functions.IsIsocele(a, b, c):
        type = "isocèle"
    else:
        type = "quelconque"

    print("Il s'agit d'un triangle", type)

# Triangle Rectangle 
print("\n3, 4, 5 :")
Triangles(3, 4, 5)

# Triangle Rectangle Isocèle
print("\n3, 3, sqrt(18) :")
Triangles(3, 3, math.sqrt(18))

# Triangle Equilatéral
print("\n2, 2, 2 :")
Triangles(2, 2, 2)

# Triangle Isocèle
print("\n2, 2, 5 :")
Triangles(2, 2, 5)

# Triangle Quelconque
print("\n5, 2, 8 :")
Triangles(5, 2, 8)
