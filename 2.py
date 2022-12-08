# !/usr/bin/env python3
from random import randint
import sys
import math
sys.setrecursionlimit(2000)

def fast_pow(b, k, n):
  if k == 0:
    return 1
  w = 1
  while k > 0:
    if k % 2 == 1:
      w = (w * b) % n
    b = (b * b) % n
    k //= 2
  return w

def is_prime(n, k=20):
  if n == 1:
    return False

  for _ in range(k):
    i = randint(2, n)
    if fast_pow(i, n - 1, n) != 1:
      return False
  return True

def is_square(x, p):
  if x % p == 0:
    return True
  else:
    return legendre(x, p) == 1

def generate_random_prime(k = 91):
  return 2074722246773485207821695222107608587480996474721117292752992589912196684750549658310084416732550077
  while True:
    p = randint(2**(k-1), 2**k-1)
    if is_prime(p):
      return p

def generate_random_curve():
  p = generate_random_prime(91)
  while True:
    A = randint(0, p-1)
    B = randint(0, p-1)
    y = (4 * fast_pow(A, 3, p) + 27 * fast_pow(B, 2, p)) % p
    if y != 0:  
      return (A, B, p)

A, B, p = generate_random_curve()

def f(x, A, B):
  return (fast_pow(x, 3, p) + A * x + B) % p


def find_random_point(A, B, p):
  while True:
    x = randint(0, p-1)
    y = (x^3 + A*x + B) % p
    if fast_pow(y, (p-1)//2, p) == 1:
      y1 = fast_pow(y, (p+1)//4, p)
      return (x, y1)


x, y = find_random_point(A, B, p)

def calculate_opposite_point(x, y):
  return (x, -y)

x, o_y = calculate_opposite_point(x, y)

def calculate_point_sum(P, Q, p, A, B):
  x1, y1 = P
  x2, y2 = Q

  if P == calculate_opposite_point(x2, y2):
    return (float('inf'), float('inf'))

  if P != Q:
    m = ((y2 - y1) / (x2 - x1)) % p
    x3 = (fast_pow(m, 2, p) - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)
  
  if P == Q:
    m = ((3 * fast_pow(x1, 2, p) + A) / 2 * y1) % p
    x3 = (fast_pow(m, 2, p) - 2 * x1) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

R = calculate_point_sum((x, y), (x, y), p, A, B)