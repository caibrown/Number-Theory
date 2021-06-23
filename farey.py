# Farey Sequence (sorted)

import numpy as np
import fractions as frac

n = int(input("Enter a positive integer:"))
seq = []

# Build list; keep only simplified fractions
for j in range(1, n+1):
    for k in range(j+1, n+1):
        if np.gcd(j,k) == 1: seq.append(frac.Fraction(j,k))
        
seq.sort() # Put in ascending order

# Format for printing
for term in range(0,len(seq)):
    seq[term] = str(seq[term])

# Add first and last terms, determine number of elements
seq.insert(0,"0/1"); seq.append("1/1") 
length = len(seq)

print("Farey Sequence of order", n, "is" )
print(seq)
print("Number of elements:", length)
