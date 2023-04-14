from classes.whiteshield import WShield

def GetDimensions():
    width = input("Selectionne une largeur > ")
    height = input("Selectionne une hauteur > ")

    try:
        width = int(width)
        height = int(height)
    except:
        print("La longueur et la largeur doivent être des nombres entier.")
        return GetDimensions()
    else:
        return (width, height)
    finally:
        print("\n")

def DrawRectangle(width, height):
    if (WShield.IsInt(width, 3) and WShield.IsInt(height, 2)):
        (vDelimiter, hDelimiter) = ("|", "-")

        for h in range(height):
            line = vDelimiter

            if h == 0 or h == (height-1):
                line += hDelimiter * (width-2)
            else:
                line += " " * (width-2)

            line += vDelimiter

            print(line)
    else:
        print("\nLargeur minimum : 3\nLongueur minimale : 2")

