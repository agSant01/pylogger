import string
import random


def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
