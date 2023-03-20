import rsa
from rsa import digital_signature

def rsa_example():
    print('Enter message to be encrypted.')
    message = input('> ')
    Pk, pk = rsa.generate_Pk_and_pk(11, 13)
    encrypted_message = rsa.encrypt_string(message, Pk)
    decrypted_message = rsa.decrypt_string(encrypted_message, pk)
    print('Original message: ' + message)
    print('Encrypted message: ' + ''.join([chr(integer) for integer in encrypted_message]))
    print('Decrypted message: ' + decrypted_message)

def digital_signature_example():
    print('Enter message to be signed.')
    message = input('> ')
    Pk, pk = digital_signature.generate_Pk_and_pk(11, 13)
    signature = digital_signature.sign_string(message, pk)
    signature_valid = digital_signature.verify_signature(signature, message, Pk)
    print('Original message: ' + message)
    print('Signature: ' + ''.join([chr(integer) for integer in signature]))
    print('Signature validity: ' + str(signature_valid))

if __name__ == '__main__':
    rsa_example()
    print('')
    digital_signature_example()