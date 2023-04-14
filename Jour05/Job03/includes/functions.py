from classes.whiteshield import WShield

def Draw(size):
    if WShield.IsInt(size, 5):
        width = size+1
        height = size

        (border, fil) = ("|", "#")
        replaceIndex = width-2

        print("+" + ("-" * (width-1)) + "+")

        for i in range(height):

            line = fil * (width-2) 
            line = line[0:replaceIndex-i:] + " " + line[replaceIndex-i::]

            print(f"{border}{line}{border}")

        print("+" + ("-" * (width-1)) + "+")