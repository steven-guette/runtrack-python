IsMultipleOfThree = lambda num: (num > 0 and num % 3 == 0)
IsMultipleOfFive = lambda num: (num > 0 and num % 5 == 0)

def DisplayNumbers():
    for i in range(101):
        if IsMultipleOfFive(i) and IsMultipleOfThree(i):
            print("FizzBuzz")
        elif IsMultipleOfFive(i):
            print("Buzz")
        elif IsMultipleOfThree(i):
            print("Fizz")
        else:
            print(i)

DisplayNumbers()