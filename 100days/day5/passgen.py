#exercise 1 : calculate the average heights
# num = int(input("Enter the number of students: "))
# height = []
# print("Enter the height of each student: ")
# for i in range(num):
#     height.append(float(input(" ")))
# tot = 0
# for i in range(len(height)):
#     tot += height[i]
# avg = tot/len(height)
# print(f"The average height is {avg}")

#Exercise 2 : find the maximum value from a list withour using the max function
# num = int(input("How many students are there?: "))
# scores = []
# print("Enter the score of each student: ")
# for i in range(num):
#     scores.append(int(input(" ")))
# if(num == 1):
#     print("There's only one student so he/she will have the highest score")
# else:
#     for i in range(len(scores)):
#         for j in range(len(scores)):
#             if(scores[i] > scores[j]):
#                 gnum = scores[i]
#             else:
#                 break
#     print(f"The greatest score is {gnum}")

#Exercise 3 : Calculate the sum of all the even numbers from  1 to 100
# tot = 0
# for i in range(2,101,2):
#     tot += i
# print(tot)

#Exercise 4 : Fizz Buzz
# for i in range(1,101):
#     if(i%3 == 0):
#         if(i%5 == 0):
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif(i%5 == 0):
#         print("Buzz")
#     else:
#         print(i)

#Main project of the day : PyPassword Generator
# import random
# import string
# print("Welcome to the PyPassword Generator")
# let = int(input("How many letters do you want?: "))
# sym = int(input("How many symbols do you want in your password?: "))
# num = int(input("How many numbers do you want in the password?: "))
# symbols = ["!","@","#","$","%","^","&","*"]
# password = ""

#The below snippet of code is the easy or beginner level of the password generator

# for i in range(let):
#     randn = random.randint(0,26)
#     password += string.ascii_lowercase[randn] 
# for i in range(sym):
#     randn = random.randint(0,7)
#     password += symbols[randn]
# for i in range(num):
#     randn = random.randint(0,101)
#     password += str(randn)
# print(f"Your generated password is {password}")

#The below snippet of code is the hard or advanced level of the password generator

# passw = []
# for i in range(let):
#     rand = random.randint(0,25)
#     passw.append(string.ascii_lowercase[rand])
# for i in range(sym):
#     rands = random.randint(0,sym)
#     passw.append(symbols[rands])
# for i in range(num):
#     randn = random.randint(0,9)
#     passw.append(str(randn))
# for i in range(let+sym+num):
#     frand = random.randint(0,((let+sym+num)-1))
#     password += passw[frand]
# print(f"The generated password is {password}")