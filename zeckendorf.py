# Given a positive integer n, finds its Zeckendorf representation

n = int(input("Enter a positive integer:"))

# build list of fibonacci numbers
fib = [1,2]
for i in range (1,n):
    newfib = fib[i]+fib[i-1]
    if newfib > n:
        break # we don't need fib nums bigger than n!
    fib.append(newfib) 

fib = fib[::-1] # put list in descending order

zeck = fib[0] # initialize sum with highest fib num
sol = [zeck]

for i in range (1, len(fib)):
    if (zeck + fib[i]) <= n:
        zeck = zeck + fib[i]
        sol.append(fib[i])
        continue
    else:
        continue

# format for printing
val = str(n) + " = "
for i in range(0, len(sol)):
    if i != len(sol)-1:
        val = val + str(sol[i])+ " + "
    else:
        val = val + str(sol[i])

print("Zeckendorf solution for", n, ":\n", val )
