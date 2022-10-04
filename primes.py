"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    ctr = 0

    while ctr < number_of_primes:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False

        if prime:
            list.append(num)
            ctr +=1
            
        num = num + 1

    return list


