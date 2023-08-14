import string
from Crypto.Util.number import *
l = list(string.ascii_lowercase) + [' ']

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def agenerate(j, n, k=1):
    for i in range(j, n, k):
        if gcd(i, n) == 1:
            return i    

def encode(text):
    q = getPrime(5)
    g = getPrime(10)
    a = agenerate(2, q)
    h = g**a % q
    plain = text.lower()
    k = agenerate(q, 1, -1)
    s = h**k % q
    p = g**k % q
    cipher = []
    for i in plain:
        cipher.append(str(s*l.index(i)))
    cipher = ' '.join(cipher)
    print('The encrypted message as numbers is',cipher)
    print('Function value:', p)
    return cipher, a, q, p

def decode(c, a, q, p):
    cipher = list(map(int, c.split()))
    sn = p**a % q
    decipher = ''
    for i in cipher:
        decipher += l[i//sn]
    print('The decrypted text is', decipher)
    return decipher