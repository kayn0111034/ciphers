
import collections
import string
import time

"""some encryption methods I wanted to create as a fun project
"""


def caesar_cipher(text,rotate_num):
    """Caesar Cipher. Rotates string x amount. x amount is defined by
    """
    #Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.

    upper_value=collections.deque(string.ascii_uppercase) #upper_value = the ascii uppercase string
    lower_value=collections.deque(string.ascii_lowercase) #lower_value = the ascii lowercase string

    upper_value.rotate(rotate_num) #rotates upper ascii string
    lower_value.rotate(rotate_num) #rotates lower ascii string

    upper=''.join(upper_value)
    lower=''.join(lower_value)

    return text.translate(str.maketrans(string.ascii_uppercase,upper)).translate(str.maketrans(string.ascii_lowercase,lower))


print("(0) Caesar Cipher")
choose=int(input("Which cipher do you want to use?"))

if choose==0:
    text=input("Please enter text for the encryption: ")
    rotate_num=int(input("How many times would you like to rotate your text?"))
    start = time.time()
    print(caesar_cipher(text,rotate_num))
    end = time.time()
    print(f"It took {end-start} seconds to encrypt your text")
else:
    text=input("Please enter text for the encryption: ")
    rotate_num=int(input("How many times would you like to rotate your text?"))
    start = time.time()
    print(caesar_cipher(text,rotate_num))
    end = time.time()
    print(f"It took {end-start} seconds to encrypt your text")



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
