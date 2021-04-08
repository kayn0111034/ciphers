
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



def ascii_cipher(text,rotate_num):
    """caesar cipher but the all ascii characters except whitespace and reoccuring letters
    """
    letters=collections.deque(string.ascii_letters)
    numbers=collections.deque(string.digits)
    punctuation=collections.deque(string.punctuation)

    characters=collections.deque(letters+numbers+punctuation)
    compare=collections.deque(letters+numbers+punctuation)

    characters.rotate(2)

    compared=''.join(compare)
    moved_string= ''.join(characters)

    return text.translate(str.maketrans(compared,moved_string))

def reverse_cipher(text):
    reversed=text[::-1]
    return reversed

def binary_represent(text):
    input=text
    binary=' '.join(format(ord(i), '08b') for i in input)
    print(binary)

def XOR_cipher(text,k):
    cipher_text=[]
    if len(text) == len(k):
        plaintext=binary_represent(text)
        key=binary_represent(k)
        print(plaintext)
        print(key)
        i=0
        for j in range(len(text)):
            if plaintext[i]==key[i]:
                cipher_text.append('0')
                i+=1
            else:
                cipher_text.append('1')
                i+=1
        print(cipher_text)
    else:
        raise IndexError

binary_represent('654321')
XOR_cipher('123456','654321')

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
