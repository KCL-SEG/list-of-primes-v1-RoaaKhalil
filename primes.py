"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

     n = 2
    while len(list) != count:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            list.append(n)
        n += 1
    #for n in range(1, number_of_primes + 1):
        #for i in range(2, n + 1):
            #if n % i != 0:
                #\list.append(n)
    return list