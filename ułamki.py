#skrócanie
from math import gcd
a, b = int(input()), int(input())
dz = gcd(a, b)
x = a // dz
y = b // dz
print(f"{a}/{b} = {x}/{y}")

#liczba na mianową i szkrócić
from math import gcd
a, b = int(input()), int(input())
dz = gcd(a, b)

c = a // b
l = a % b
m = b

x = l // dz
y = m // dz

print(f"{a}/{b} = {c} {x}/{y}")

#dodawanie
a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = b, d
iloczyn = x * y
while y > 0:
    x, y = y, x % y
nww = iloczyn // x
e = nww // b * a
f = nww // d * c
g = e + f
print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")

#odejmowanie
a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = b, d
iloczyn = x * y
while y > 0:
    x, y = y, x % y
nww = iloczyn // x
e = nww // b * a
f = nww // d * c
g = e - f
print(f"{a}/{b} - {c}/{d} = {e}/{nww} - {f}/{nww} = {g}/{nww}")

#mnożenie
a,b = map(int, input().split())
c,d = map(int, input().split())
gora3 = a * c
dol3 = b * d
print(f"{a}/{b} * {c}/{d} = {gora3}/{dol3}")

#dzielenie
a,b = map(int, input().split())
c,d = map(int, input().split())
gora3 = a * d
dol3 = b * c
print(f"{a}/{b} : {c}/{d} = {gora3}/{dol3}")
