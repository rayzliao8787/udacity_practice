a1 = input("a1: ")
a2 = input("a2: ")
b1 = input("b1: ")
b2 = input("b2: ")
c1 = input("c1: ")
c2 = input("c2: ")
l = [int(a1), int(a2), int(b1), int(b2), int(c1), int(c2)]
Greatest = max(l)
Least = min(l)
m = 0
p = int(b1) - int(a2)
q = int(c1) - int(b2)

if p > 0:
    m += p
if q > 0:
    m += q

Ans = str(((Greatest - Least) + 1)- m)
print ("The length is " + Ans + " units.")