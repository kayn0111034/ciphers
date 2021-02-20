
import collections
import string
import time

"""some encryption methods I wanted to create as a fun project
"""


def caesar_cipher(text,rotate_num):
    """Caesar Cipher. Rotates string x amount. x amount is defined by rotate num
    """
    #Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.

    upper_value=collections.deque(string.ascii_uppercase) #upper_value = the ascii uppercase string
    lower_value=collections.deque(string.ascii_lowercase) #lower_value = the ascii lowercase string
    digit=collections.deque(string.digits)

    upper_value.rotate(rotate_num) #rotates upper ascii string
    lower_value.rotate(rotate_num) #rotates lower ascii string
    digit.rotate(rotate_num)

    upper=''.join(upper_value)
    lower=''.join(lower_value)
    digit=''.join(digit)

    return text.translate(str.maketrans(string.ascii_uppercase,upper)).translate(str.maketrans(string.ascii_lowercase,lower)).translate(str.maketrans(string.digits,digit))



def ascii_cipher():
    """caesar cipher but the all ascii characters except whitespace and reoccuring letters
    """
    letters=collections.deque(string.ascii_letters)
    numbers=collections.deque(string.digits)
    punctuation=collections.deque(string.punctuation)

    characters=collections.deque(letters+numbers+punctuation)

    rotated=characters.rotate(2)

    before_rotate_string = ''.join(characters)



    #rot_string=''.join(rotated)


    print(rotated)
    print(before_rotate_string)
    print(characters)
    #return text.translate(str.maketrans(before_rotate_string,rot_string))

ascii_cipher()
#testing ascii letters & deque's rotate func
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
#
# a = collections.deque()
# print(a)
# a.append("a")
# print(a)
# a.append('b')
# print(a)
# a.rotate(1)
# print(a)
# b="".join(a)
# print(b)
