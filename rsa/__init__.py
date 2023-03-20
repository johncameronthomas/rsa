import math

def generate_Pk_and_pk(p, q):
    n = p * q
    t = (p - 1) * (q - 1)
    e = 2
    while e > 1 and e < t:
        if math.gcd(e, t) == 1:
            break
        else:
            e += 1
    d = 2
    while True:
        if (d * e) % t == 1:
            break
        else:
            d += 1
    Pk = (e, n)
    pk = (d, n)
    return Pk, pk

def encrypt(m, Pk):
    e, n = Pk
    if m > n:
        raise(ValueError('m is greater than n'))
    else:
        return (m ** e) % n

def decrypt(c, pk):
    d, n = pk
    return (c ** d) % n

def encrypt_string(string, Pk):
    return [encrypt(ord(integer), Pk) for integer in string]

def decrypt_string(encrypted_string, pk, encoding='utf-8'):
    return ''.join([chr(decrypt(integer, pk)) for integer in encrypted_string])