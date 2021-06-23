# Extended Euclidean Algorithm:
# For a and b in N, finds their gcd and Bézout coefficients

ints=input("Enter two positive integers separated by a comma, the larger first:")

# Format input
a,b = ints.split(','); a = int(a); b = int(b)

# Theorem 3.14 in text
s = 0;  old_s = 1
t = 1;  old_t = 0
r = b;  old_r = a

while r > 0:
    q = old_r // r
    tmp = r;    r = old_r - q * tmp;    old_r = tmp
    tmp = s;    s = old_s - q * tmp;    old_s = tmp
    tmp = t;    t = old_t - q * tmp;    old_t = tmp

print("Greatest common divisor (gcd):", old_r)
print("Bézout coefficients:", old_s, old_t)
