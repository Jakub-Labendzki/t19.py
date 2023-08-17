# Diagnoza INF

# - WSTĘP
# 1. Oblicz sumę liczb 3-cyfrowych
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
suma = 0
ilosc = 0
for i in range(12, 100, 6):
    suma += i
    if i % 6 == 0:
        ilosc += 1
print(suma, ilosc)
# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
import random
T = [1, 2, 3, 4, 5]
for i in range(5):
  T[i] = random.randint(1000, 10000)
print(max(T))
# 4. Podaj sumę cyfr w dowolnej liczbie
a4 = input()
s4 = list(a4)
suma = 0
for i in range(len(s4)):
  suma += int(s4[i])
print(suma)
# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
a5 = input()
T5 = list(a5)
print(min(T5))
# - ALGORYTMY
# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
a6 = int(input())
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
print(is_prime(a6))
# 2. Sprawdź czy wpisana przez usera liczba jest złożona
a7 = int(input())
def zlozona(n):
  if n < 2:
    return True
  for i in range(2,n):
    if n%i == 0:
      return True
  return False
print(zlozona(a7))
# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
import math
a8 = int(input())
if math.gcd(a8, 24) == 1:
  print("TAk")
else:
  print("NIe")
# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.
a9 = input()
k = int(input())
T = list(a9)
for i in range(len(T)):
  T[i] = chr(ord(T[i]) + k)
print(T)
# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.

from math import gcd
a, b = map(int,input().split("/"))
c, d = map(int,input().split("/"))
x, y = b, d
ilocz = x * y
while y>0:
    x, y = y, x % y
nww = ilocz // x
e = (nww // b) * a
f = (nww // d) * c
g = e + f
print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")

dz = gcd(a, b)

c = g // nww
l = g % nww
m = nww

x1 = l // dz
y2 = m // dz

print(f"Mieszany: {g}/{nww} = {c} {x1}/{y2}")

x2 = g // dz
y3 = nww // dz
print(f"Nieskracalny: {g}/{nww} = {x2}/{y3}")

# 6. Znajdź NWW dwóch wpisanych przez usera liczb
a1, b1 = int(input), int(input())
iloczyn = a1 * b1
while b1 > 0:
  a1, b1 = b1, a1 % b1
nww = a1
print(iloczyn // nww)

# - KARTKA
# 1. Oblicz wartość ONP
#Przykład: 4 5 + 4 * 2
# 4
# 4 5 +
# 9
# 9 4 *
# 36 2 /
# Wynik: 18

# 2. Znajdź postać ONP dla pisanego wyrażenia
# 2
# 3
# 5
# -
# 3
# *
# /

#   k   | r
#       | 2
#       | 2 3
#       | 2 3 5
# -     | 2 3 5
# -     | 2 3 5 3
# - *   | 2 3 5 3
# - * / | 2 3 5 3
# Wynik to: 2 3 5 3 - * /

# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb

# a, b = int(input()), int(input())
# while b > 0:
#   a, b = b, a % b
# print(a)

# a  | b  | r = a % b
# 90 | 36 | 90 % 36 = 18
# 36 | 18 | 36 % 18 = 0
# 18 | 0  |
# Wynik to: 18

# a, b = int(input()), int(input())
# while a != b:
#   if a > b : a = a - b
#   if b > a : b = b - a
# print(a)

# a  | b  | r = a - b
# 36 | 28 | 36 - 28 = 8
# 8  | 28 | 28 - 8 = 20
# 8  | 20 | 20 - 8 = 12
# 8  | 12 | 12 - 8 = 4
# 8  | 4  | 8 - 4 = 4
# 4  | 4  |
# Wynik to: 4

# - NAPISY
# 1. Znajdź ilość liter C we wpisanym napisie
a0 = input()
a01 = a0.count('C')
print(a01)
# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
a02 = input()
def sprawdz(a02):
    for i in range(1, len(a02)):
        if a02[i-1] > a02[i]:
            return False
    return True
print(sprawdz(a02))
# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
a03 = input()
a04 = input()
a05 = input()
maxik = max(a03, a04, a05, key=len)
print(maxik)
