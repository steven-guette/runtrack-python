def GetNumberOfMultiples(numbers, multiple):
    multiplesQuantity = 0

    if type(numbers) == list and len(numbers) > 0:
        try:
            multiple = int(multiple)
        except:
            print("Le paramètre `multiple` doit contenir un nombre entier.")
        else:
            if (multiple > 0):
                multiplesQuantity = 0

                for number in numbers:
                    try:
                        number = int(number)
                    except:
                        continue
                    else:
                        multiplesQuantity += int((number % multiple) == 0)
            else:
                print("Le multiple choisi doit être supérieur à zéro.")

    return multiplesQuantity


L = [8, 24, 48, 2, 16]

print(f"La liste {L[:]} contient {GetNumberOfMultiples(L, 3)} multiples de 3.")