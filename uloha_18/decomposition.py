import math
# Function that decomposes an input parameter n (a natural number greater than 1) into the product of prime numbers
def decomp_into_prime_num(n):
    # Verify that the input value is correct if the input is not correct program ends.
    if n <= 1:
        exit("ERROR: Prime decomposition can only be performed for number N> 1")
    if n % 1 != 0:
        exit("ERROR: Prime decomposition can only be performed for the natural number N")  
    print("Prime number decomposition of a number {} is:".format(n))
    m = n
    exp = 0
    prime = 2
# The cycle of prime decomposition
    while n > 1:
        if n % prime == 0: # condition whether n is divisible by a prime number. It finds out if there's a same prime number once or twice
            exp += 1
            n = n/prime
        else: # print values if there is a prime number only once or more
            if exp == 1:
                print("{} x".format(prime), end = " ")
            if exp > 1:
                print("{}^{} x".format(prime, exp), end = " ")
            prime+=1
            exp = 0
    # Condition if the input value is a prime number
    if prime == m:
        print("Number {} is prime number".format(m))
    else:
        if exp == 1:
            print(prime)
        if exp > 1:
            print("{}^{}".format(prime, exp))

# run function
NATURAL_NUMBER = 100
# Verify that the input value is not integer, if its not the program ends.
if type(NATURAL_NUMBER) != int:
    exit("ERROR: Prime decomposition can only be performed for the natural number N")
decomp_into_prime_num(NATURAL_NUMBER)