from nose2.tools import *
from rsa_lukec import encryption

keys = encryption.EncryptionKeys()

private_key = keys.get_private_key()
public_key = keys.get_public_key()

encrypted = encryption.encrypt(public_key, 91)
print(encrypted)
decrypted = encryption.decrypt(private_key, encrypted)
print(decrypted)


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    print("I RAN!")
