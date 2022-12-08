import random

def gcdExtended(x, N):
	if x == 0:
		return 0, 1, N
	u1, v1, d = gcdExtended(N % x, x)
	u = v1 - (N // x) * u1
	v = u1
	return u, v, d

def gcd(x, N):
	u, v, d = gcdExtended(x, N)
	return d

def gen_key(q):
	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)
	return key

def fastPow(b, k, n):
	w = 1
	while k > 0:
		if k % 2 == 1:
			w = (w * b) % n
		b = (b * b) % n
		k //= 2
	return w % n

def encryption(msg, q, h, g):
	ct = []
	k = gen_key(q)
	s = fastPow(h, k, q)
	p = fastPow(g, k, q)
	for i in range(0,len(msg)):
		ct.append(msg[i])
	# print("g^k used= ", p)
	# print("g^ak used= ", s)
	for i in range(0, len(ct)):
		ct[i] = s * ord(ct[i])
	return ct, p

def decryption(ct, p, key, q):
	pt = []
	h = fastPow(p, key, q)
	for i in range(0, len(ct)):
		pt.append(chr(int(ct[i] / h)))
	return pt

q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = fastPow(g, key, q)

message = input("Wiadomosc: ")

ct, p = encryption(message, q, h, g)

print("Original: ", message)
print("Encrypted: ", ct)
print("Message: ", ''.join(decryption(ct, p, key, q)))