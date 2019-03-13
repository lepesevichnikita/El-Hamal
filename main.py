#!/bin/python3
from elhamal import ElHamal

def main():
    keys = ElHamal().gen_keys()
    print('keys: ', keys)
    text = input('Enter text for encryption please:')
    encrypted_text = ElHamal.encrypt(text, keys[:3])
    print('encryption result:', encrypted_text)
    decrypted_text = ElHamal.decrypt(encrypted_text, keys)
    print('Source text:', decrypted_text)


main()
