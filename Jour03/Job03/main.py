excludedNumbers = (26, 37, 88)

def DisplayNumbers(exceptions):
    for i in range(101):
        if i not in exceptions:
            print(i)

DisplayNumbers(excludedNumbers)
