def DisplayNumbers():
    numbers = ""

    for i in range(21):
        if len(numbers) == 0:
            numbers += str(i)
            continue

        numbers += " {}".format(str(i))

    print(numbers)

DisplayNumbers()