import hashlib
import rsa

def generate_Pk_and_pk(p, q):
    pk, Pk = rsa.generate_Pk_and_pk(p, q)
    return Pk, pk

def sign_string(string, pk):
    h = hashlib.new('sha512_256')
    h.update(string.encode())
    return rsa.encrypt_string(h.hexdigest(), pk)

def verify_signature(digital_signature, string, Pk):
    h_a = rsa.decrypt_string(digital_signature, Pk)
    h_b = hashlib.new('sha512_256')
    h_b.update(string.encode())
    if h_a == h_b.hexdigest():
        return True
    else:
        return False