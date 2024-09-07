import string
import random

def Password():

 len = int(input("Enter length of password:"))

 lower = string.ascii_lowercase

 upper = string.ascii_uppercase

 digit = string.digits

 symbols = string.punctuation

 str = lower + upper + digit + symbols

 password="".join(random.sample(str,len))

 print("Password is:",password)

Password()
