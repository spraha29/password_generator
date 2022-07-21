import random
import string
import secrets
num= int(input("Enter the No of digits requierd: "))
result = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))  
print("Your password is: ",result)