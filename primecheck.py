# Tests primality of an integer n

import sys, math # Fun draws nigh

while True:
    
    n = int(input("Enter a positive integer or '0' to quit:"))
    if n == 0:
        sys.exit()
    
    sqrt_n = math.floor(math.sqrt(n))

    for i in range(2, sqrt_n + 1):
        if i % 6 == 1 or i % 6 == 5:
            if n % i == 0:
                continue
            else:
                print("Prime.")
                break
