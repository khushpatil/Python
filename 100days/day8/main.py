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
def encrypt(text, shift):
    encoded_message = ""
    for letter in text:
        ind = string.ascii_lowercase.index(letter)
        while ind+shift <= len(string.ascii_lowercase):
            encoded_message += string.ascii_lowercase[ind+shift]
        if(ind+shift > len(string.ascii_lowercase)):
            encoded_message += string.ascii_lowercase[((ind+shift)-(len(string.ascii_lowercase)))-1]
    print(f"The encoded message is {encoded_message}")
while start=="encode" or "decode":
    text = input("Enter your message: ")
    shift = int(input("Enter the shift: "))
    encrypt(text,shift)

