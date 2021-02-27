import collections
import string
import random

def password_gen(letter_amount):
    letters=collections.deque(string.ascii_letters)
    numbers=collections.deque(string.digits)
    characters=collections.deque(letters+numbers)

    password=[]

    for i in range(letter_amount):
        p=random.choice(characters)
        password.append(p)

    password=''.join(password)
    print(password)
