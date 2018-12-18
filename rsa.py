# -*- coding: utf-8 -*-
import random


def eh_primo(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = random.randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True


def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = random.randint(2**(n-1), 2**n)
        if eh_primo(p, 1000):
            return p


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inverso(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_keypair(p, q):
    if p == q:
        raise ValueError('Os números não podem ser iguais')
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = inverso(e, phi)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':

    while True:
        print("1 - Encrypt")
        option = int(raw_input())

        if option == 1:
            p = generate_big_prime(5)
            q = generate_big_prime(4)

            public, private = generate_keypair(p, q)
            print("Chave publica: {0} Chave privada: {1}".format(public, private))
            message = raw_input("Escreva a mensagem à ser criptografada: ")
            encrypted_msg = encrypt(private, message)

            print("A mensagem cifrada é: ")
            plain_msg = ''.join(map(lambda x: str(x), encrypted_msg))
            print(plain_msg)

            print("2 - Decrypt")
            print("3 - Descobrir pk conhecendo n e a mensagem por brute force")
            option = int(raw_input())

            if option == 2:
                print("Decifrando mensagem com chave pública {0}".format(public))
                print("A mensagem é:")
                print(decrypt(public, encrypted_msg))

            if option == 3:
                n = public[1]
                i = 1
                while True:
                    brute_force_pk = (i, n)
                    if decrypt(brute_force_pk, encrypted_msg) == message:
                        print("Chave descoberta por meio de brute force: {0}".format(brute_force_pk))
                        break
                    else:
                        i = i + 1

            else:
                print("Digite uma opção valida")
        else:
            print("Digite uma opção valida")
