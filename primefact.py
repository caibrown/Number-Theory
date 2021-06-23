# Given an integer, finds its prime factorization via simple trial division
import math, sympy, sys

another = 'y' # Indefinite loop condition
print("FUNdamental Theorem of Arithmetic")
while True:
    n = int(input("Enter an integer:")); q = math.ceil(math.sqrt(n))

    factors = []
    for k in range(1, q+1):
        if sympy.isprime(k) == True: factors.append(k)

    sol = [n] # For printing, later

    for factor in factors:
        if n % factor == 0: # If the factor divides n evenly
            count = 0
            while n % factor == 0:
                n = n / factor
                count += 1 # Exponent on factor in solution
            sol.append(str(factor)+"^"+str(count))
    if n != 1: sol.append(int(n)) # There's a prime factor > q
            
    # Format for printing
    factorization = str(sol[0]) + " = "
    for i in range(1, len(sol)):
        if i != len(sol)-1:
            factorization = factorization + str(sol[i]) + " * "
        else:
            factorization = factorization + str(sol[i])
    print("Prime factorization for", sol[0], ":\n", factorization)
    
    another = input("Huzzah! Another? y/n:") # weeee
    if another == 'n': sys.exit()
