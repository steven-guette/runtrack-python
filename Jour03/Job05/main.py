def IsPrimeNumber(number):
    isPrime = True

    for i in range(2, 11):
        if i != number and (number % i) == 0:
            isPrime = False
            break

    return isPrime

for i in range(2, 1001):
   if IsPrimeNumber(i):
       print(i)