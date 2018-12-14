
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inverso(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx


def eh_primo(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (eh_primo(p) and eh_primo(q)):
        raise ValueError('Ambos numeros digitados devem ser primos.')
    elif p == q:
        raise ValueError('Os números digitados não podem ser iguais')
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = inverso(e, phi)
    return ((e, n), (d, n))