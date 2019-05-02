import string
from random import choice


def generate_random_string(size):
    val = "".join(choice(string.ascii_lowercase) for i in range(size))
    return val
