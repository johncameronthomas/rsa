import math
import hashlib

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
    return(Pk, pk)

def encrypt(m, Pk):
    e, n = Pk
    if m > n:
        raise(ValueError('m is greater than n'))
    return((m ** e) % n)

def decrypt(c, pk):
    d, n = pk
    return((c ** d) % n)

def encrypt_string(string, Pk):
    return([encrypt(ord(integer), Pk) for integer in string])

def decrypt_string(encrypted_string, pk, encoding='utf-8'):
    return("".join([chr(decrypt(integer, pk)) for integer in encrypted_string]))

def sign_string(string, Pk): # Pk is kept private by authority
    h = hashlib.new('sha512_256')
    h.update(string.encode())
    return(encrypt_string(h.hexdigest(), Pk))

def verify_signature(digital_signature, string, pk): # ok is left public by authority
    h_a = decrypt_string(digital_signature, pk)
    h_b = hashlib.new('sha512_256')
    h_b.update(string.encode())
    if h_a == h_b.hexdigest():
        return(True)
    else:
        return(False)