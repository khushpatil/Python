# def greet():
#     print("Hello, world!\nThis is Khush Patil\nI'm the stronkest nigger here")
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}!\nHope you have a good day {name}")
# greet_with_name("Khush")

# def greet_with(name, location):
#     print(f"Hello {name}!\nGreetings from {location}")
# greet_with(location = "India", name = "khush")

#Paint cans calculator
# import math
# height = float(input("Enter the height of your wall: "))
# breadth = float(input("Enter the breadth of your wall: "))
# def area_calc(height, breadth):
#     area = height*breadth
#     return area
# cans = math.ceil(area_calc(height,breadth)/5)
# print(f"You would need approximately {cans} cans to cover the wall")

#Prime number checker
# num = int(input("Enter your number: "))
# def prime_checker(num):
#     check = 0 
#     for i in range(2,num):
#         if(num%i==0):
#             check += 1
#     if(num == 0):print("0 is in a limbo")
#     elif(check>0):print("The number is not a prime number")
#     else:print("The number is a prime number")
# prime_checker(num)

#making the caesar cipher
import string
start = input("Type encode to start encoding or decode to decode a message: ")
text = input("Enter your message: ")
shift = int(input("Enter the shift: "))
if(start == "encode" or "decode"):
    encode = True
else:encode = False
def encrypt(text, shift):
    encoded_message = ""
    new_alphabet = []
    while encode :
        #The below code is to create a new alphabet with the given shift
        for i in range(len(string.ascii_lowercase)):
            while i+shift <= len(string.ascii_lowercase):
                new_alphabet.append(string.ascii_lowercase[i+shift])
            else:
                for j in range(len(string.ascii_lowercase)-len(new_alphabet)):
                    new_alphabet.append(string.ascii_lowercase[j])
        for letter in text:
            ind = string.ascii_lowercase.index(letter)
            encoded_message += new_alphabet[ind]
        print(f"The encoded message is {encoded_message}")
encrypt(text, shift)