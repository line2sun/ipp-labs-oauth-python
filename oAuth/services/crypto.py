from random import choice
import hashlib
from string import ascii_letters, digits


def generate_salt(length=128):
    """ Generates a random string of specified length.
    Contains letters and digits. Default length is 10.
    :param length: the length of generated string.
    :type length: int
    :return: string
    """
    return ''.join(choice(ascii_letters + digits) for i in range(length))


def hash(password):
    """ Hashes the given password.
    :param password: a string
    :return:
    """
    salt = generate_salt()
    md5 = hashlib.new('md5')
    md5.update(salt + password)
    return salt, md5.hexdigest()


def are_same_hashes(_hash, salt, text):
    """ Checks if the given hash has been generated form the given text
    using provided salt.
    """
    md5 = hashlib.new('md5')
    md5.update(salt + text)

    return _hash == md5.hexdigest()

if __name__ == '__main__':
    salt = "VmtnALTBNfC8IpjJf6a07aBr6yY9cdMMerYziPabQN4lToAXC12alT4GedHyJpmoXl6RevfFxqvy8CTTbQjdhZTTeVGzti8niLN5mEfmNSCQfo4z3k09BMlcIuAeIwlf"
    _hash = "f1a97302c86f3512007b0b736e152b14"
    text = 'test'
    print are_same_hashes(_hash, salt, text)
