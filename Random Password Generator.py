import string
import random

Length=int(input("Enter The Length Of Your Password :"))

Lowercase=string.ascii_lowercase

Uppercase=string.ascii_uppercase

Digit=string.digits

Special=string.punctuation

str=Lowercase+Uppercase+Digit+Special

pwd=random.sample(str,Length)

password="".join(pwd)

print("Your password is :",password)