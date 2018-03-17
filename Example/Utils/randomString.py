import string
from random import choice


def randomString(size):
    val = "".join(choice(string.ascii_lowercase) for i in range(size))
    return val
