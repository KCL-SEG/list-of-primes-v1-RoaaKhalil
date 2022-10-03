"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    ctr = 2
    list.append(2)
    while ctr <= number_of_primes:
        num = nextPrime(num)
        list.append(num)
        ctr +=1

    return list


def nextPrime(num):
    while True:

        num += 1

        for i in range (2, num):
            if num % i == 0:
                break

            else:
                return num