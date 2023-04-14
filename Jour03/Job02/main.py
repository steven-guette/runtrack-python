isOddNumber = lambda num: (num % 2 == 1)

def DisplayOddNumbers():
    numbers = ""

    for i in range(21):
        if (isOddNumber(i)):
            if len(numbers) == 0:
                numbers += str(i)
                continue

            numbers += " {}".format(str(i))

    print(numbers)

DisplayOddNumbers()