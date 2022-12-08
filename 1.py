# !/usr/bin/env python3
import random
import sys
sys.setrecursionlimit(2000)

# Zadanie 1.
def gcdExtended(x, N):
  if x == 0:
    return 0, 1, N
  u1, v1, d = gcdExtended(N % x, x)
  u = v1 - (N // x) * u1
  v = u1
  return u, v, d


def odwrotnosc(x, y):
  u, v, d = gcdExtended(x, y)
  if d != 1:
    return False
  else:
    return u % y


# # Zadanie 2.
def fastPow(b, k, n):
  w = 1
  while k > 0:
    if k % 2 == 1:
      w = (w * b) % n
    b = (b * b) % n
    k //= 2
  return w % n


# Zadanie 3.
def fermat(n, k=1000):
  if n == 1:
    return False

  count = 0
  for _ in range(k):
    i = random.randint(2, n)
    if fastPow(i, n - 1, n) != 1:
      return False
    count += 1
  return True, 1 - 1 / count

# Zadanie 4.
def resta(a, p = 3):
  x = fastPow(a, (p - 1) / 2, p)
  print(x)


# resta(35201546659608842026088328007565866231962578784643756647773109869245232364730066609837018108561065242031153677, 100000)

# Zadanie 2.
def randomWithNDigits(n):
  rangeStart = 10 ** (n - 1)
  rangeEnd = (10 ** n) - 1
  return random.randint(rangeStart, rangeEnd)

def findPQ():
  while True:
    p = randomWithNDigits(200)
    if fermat(p, 10):
      q = 2 * p - 1
      if fermat(q, 10):
        return p, q


print(findPQ())

p = 31468156130196181686775766196702255137270599961740572809246495752014589162295620086444858595123052317230827824565913763441926340824333418086674266875197320673421132505310507623041860913462064290797813
q = 2 * p - 1
