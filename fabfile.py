import random
import string

from fabric.api import warn, local
from fabric.colors import green


def generate_new_secret_key(key_length=32):
    """
    Generate new secret key
    """

    symbols = string.ascii_letters + str(string.digits) + '!@#$%^&*()+-'
    secret_key = "".join(random.sample(symbols*2, key_length))
    warn("New secret key: " + green(secret_key))
    return secret_key


def generate_secret_key_file():
    template = """# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{}'
""".format(generate_new_secret_key(key_length=64))
    with open('settings/secret_key.py', 'w') as f:
        f.write(template)
