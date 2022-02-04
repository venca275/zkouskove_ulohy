# function that decomposes an input parameter n (a natural number greater than 1) into the product of prime numbers
def decomp_into_prime_num(n):
    if n <= 1:
        exit("CHYBA: Prvočíselný rozklad lze provést pouze pro číslo N > 1")
    if n % 1 != 0:
        exit("CHYBA: Prvočíselný rozklad lze provést pouze pro přirozené číslo N")
    
    print("Prvočíselný rozklad čísla {} je:".format(n))
    m = n
    num = 0
    exp = 0
    prime = 2

    while n > 1:
        if num == 0:
            num = prime
            prime += 1
        
        if n % num == 0:
            exp += 1
            n = n/num
        else:
            if exp == 1:
                print("{} x".format(num), end = " ")
            if exp > 1:
                print("{}^{} x".format(num, exp), end = " ")
            
            num = 0
            exp = 0
    if num == m:
        print("Číslo {} je prvočíslo".format(m))
    else:
        if exp == 1:
            print(num)
        if exp > 1:
            print("{}^{}".format(num, exp))
        
# run function
NATURAL_NUMBER= 100
if type(NATURAL_NUMBER) != int:
    exit("CHYBA: Prvočíselný rozklad lze provést pouze pro přirozené číslo N")
decomp_into_prime_num(NATURAL_NUMBER)