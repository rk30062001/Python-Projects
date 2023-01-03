# Student_Name = str(input("Enter The Name:"))
# Student_Subject =
# for Name in range(5):
#     print(Name)


# students=[]
# for num in range(3):
#     x=input("Enter name of students: ")
#     students.append(x)


# Subjects={'Math:','/n',
#            'English:'
#            'Physics:'
#            'Chemistry:'
#            'Programming:'}
# print(Subjects)

# student = input(" How many students ")
# list = []
# for i in range(3):
#     n = input("Enter the students name:")
# dict={'math','English','Physics','Chemistry','Programming'}
# print(dict)
# for j in range(5):
#     m = int(input("Enter marks:"))
#     print(dict,"\n")
#     print('math:=',m)


# N = input("Enter the Name:")
# dict = {'Math':65,'English':85,'Physics':75,'Chemistry':78,'Programming':88}
# print(sum(dict.values())*100/500,"%")
# print(max(dict.values()))
# print(dict.keys())

# --------------------------------Write a program to print a calculator--------------------------------
# x = int(input("Enter the number:"))
# y = int(input("Enter the number:"))
# operator = input("Enter the operator:")
# #
# if (operator == '+'):
#      print("Addition", x + y)
# elif (operator == '-'):
#      print("subtraction", x - y)
# elif (operator == '*'):
#      print("multiplication", x * y)
# elif (operator == '/'):
#      print("Division", x / y)
# elif (operator == '%'):
#      print("Modulus",x % y)
# else:
#      print("Invalid")

# Using Function
# def fun(x, y):
#     print("Addition:",x + y)
#     print("Subtraction:",x - y)
#     print("Multiplication:",x * y)
#     print("Division:",x / y)
#     print("Modulus:",x % y)
#
#
# fun(10, 20)


# def fun():
#     x = int(input("Enter the number:"))
#     y = int(input("Enter the number:"))
#     print("Addition:", x + y)
#     print("Subtraction:", x - y)
#     print("Multiplication:", x * y)
#     print("Division:", x / y)
#     print("Modulus:", x % y)
#
#
# fun()

# def add(x,y):
#     return(x+y)
# def sub(x,y):
#     return(x-y)
# def mul(x,y):
#     return(x*y)
# def div(x,y):
#     return(x/y)
# def mod(x,y):
#     return(x%y)
#
#
# print(add(5,6))
# print(sub(6,5))
# print(mul(5,5))
# print(div(25,5))
# print(mod(25,5))


# ------------------------------------Write a program for quiz------------------------------------

# print("Welcome to Quiz Game")
# Question1 = input("Who is the prime Minister if India?\na. Narendra Modi \nb. Amit sha \nc. Rajnath singh \nd. Yogi "
#                    "Adityanath \nAnswer:")
# if (Question1 == "a." or Question1 == "Narendra modi"):
#      print("Correct")
#      print("\n")
# else:
#      print("Incorrect")
#      print("\n")
#
# Question2 = input("Who is the captain of men's Indian cricket team?\na. Virat Kohli \nb. KL Rahul \nc. Rohit Sharma "
#                   "\nd. Rishab pant \nAnswer:")
# if (Question2 == "c." or Question2 == "Rohit Sharma"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question3 = input("Who is the CM of Uttar Pradesh?\na. Akhlesh Yadav \nb. Yogi Adityanath \nc. Amrendra singh \nd. "
#                   "Rahul Gandhi \nAnswer:")
# if (Question3 == "b." or Question3 == "Yogi Adtiyanath"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question4 = input("Who is the Founder of Google?\na. Sundar pichai \nb. Larry page \nc. Elon musk \nd. Ambani \nAnswer:")
# if (Question4 == "b." or Question4 == "Larry page"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question5 = input("Who is the CEO of Google?\na. Larry page \nb. Elon musk \nc. Sundar pichai \nd. Adani \nAnswer:")
# if (Question5 == "c." or Question5 == "Sundar pichai"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question6 = input("Who is the founder of Microsoft?\na. Mark Zuckerburg \nb. Bill Gates \nc. Steve jobs \nd. Jack "
#                   "dorcy \nAnswer:")
# if (Question6 == "b." or Question6 == "Bill Gates"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question7 = input("Who is the founder of Amazon?\na. Jeff Bezos \nb. Elon musk \nc. Ratan Tata \nd. Mark Zuckerburg "
#                   "\nAnswer:")
# if (Question7 == "a." or Question7 == "Jeff Bezos"):
#     print("correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question8 = input("Who is the founder of TATA Group?\na. Ambani \nb. Adani \nc. Ratan Tata \nd. Anand Mahindra "
#                   "\nAnswer:")
# if (Question8 == "c." or Question8 == "Ratan Tata"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question9 = input("Who is the president of France?\na. Emmanuel Macron \nb. Putin \nc. Rishi Sunak \nd. Joe biden "
#                  "\nAnswer:")
# if (Question9 == "a." or Question9 == "Emmanuel Macron"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")
#
# Question10 = input("Who is the president of India?\na. Ramnath Govind \nb. Droupadi Murmur \nc. Amit sha \nd. Indra "
#                    "Gandhi \nAnswer:")
# if (Question10 == "b." or Question10 == "Droupadi Murmur"):
#     print("Correct")
#     print("\n")
# else:
#     print("Incorrect")
#     print("\n")

# \\\\\\\\\\\-----------------------------------For Scoring------------------------------------////////////
# print("Welcome to Quiz Game")
# score = 0
# Question1 = input("1. Who is the prime Minister if India?\na. Narendra Modi \nb. Amit sha \nc. Rajnath singh \nd. Yogi "
#                    "Adityanath \nAnswer:")
# if (Question1 == "a." or Question1 == "Narendra modi"):
#      score+=10
#      print("Correct")
#      print("score:", score)
#      print("\n")
#
# else:
#      print("Incorrect")
#      print("score:=",0)
#      print("\n")
#
#
# Question2 = input("2. Who is the captain of men's Indian cricket team?\na. Virat Kohli \nb. KL Rahul \nc. Rohit Sharma "
#                   "\nd. Rishab pant \nAnswer:")
# if (Question2 == "c." or Question2 == "Rohit Sharma"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question3 = input(" 3. Who is the CM of Uttar Pradesh?\na. Akhlesh Yadav \nb. Yogi Adityanath \nc. Amrendra singh \nd. "
#                   "Rahul Gandhi \nAnswer:")
# if (Question3 == "b." or Question3 == "Yogi Adtiyanath"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question4 = input("4. Who is the Founder of Google?\na. Sundar pichai \nb. Larry page \nc. Elon musk \nd. Ambani "
#                   "\nAnswer:")
# if (Question4 == "b." or Question4 == "Larry page"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question5 = input("5. Who is the CEO of Google?\na. Larry page \nb. Elon musk \nc. Sundar pichai \nd. Adani \nAnswer:")
# if (Question5 == "c." or Question5 == "Sundar pichai"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question6 = input("6. Who is the founder of Microsoft?\na. Mark Zuckerburg \nb. Bill Gates \nc. Steve jobs \nd. Jack "
#                   "dorcy \nAnswer:")
# if (Question6 == "b." or Question6 == "Bill Gates"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question7 = input("7. Who is the founder of Amazon?\na. Jeff Bezos \nb. Elon musk \nc. Ratan Tata \nd. Mark Zuckerburg "
#                   "\nAnswer:")
# if (Question7 == "a." or Question7 == "Jeff Bezos"):
#     score+=10
#     print("correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question8 = input("8. Who is the founder of TATA Group?\na. Ambani \nb. Adani \nc. Ratan Tata \nd. Anand Mahindra "
#                   "\nAnswer:")
# if (Question8 == "c." or Question8 == "Ratan Tata"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question9 = input("9. Who is the president of France?\na. Emmanuel Macron \nb. Putin \nc. Rishi Sunak \nd. Joe biden "
#                  "\nAnswer:")
# if (Question9 == "a." or Question9 == "Emmanuel Macron"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
#
# Question10 = input("10. Who is the president of India?\na. Ramnath Govind \nb. Droupadi Murmur \nc. Amit sha \nd. Indra "
#                    "Gandhi \nAnswer:")
# if (Question10 == "b." or Question10 == "Droupadi Murmur"):
#     score+=10
#     print("Correct")
#     print("score:=",score)
#     print("\n")
# else:
#     print("Incorrect")
#     print("score:=",0)
#     print("\n")
# # ----------Final_Message---------
# if(score>=90):
#     print(" Congratulation! You are Eligible for Next Round ")
# else:
#     print(" Sorry! You are not Eligible for Next Round ")

# Second method for Quiz Question.
# score = 0
# Question1 = str(input("Who is the prime minister of india:"))
# a = 'Narender Modi'
# b = 'Amit sha'
# c = 'Rajnath singh'
# d = 'Yogi Adityanath'
# #
# if(Question1 == "a"):
#      score += 10
#      print("correct")
#      print("score:=", score)
#      print("\n")
# else:
#      print("Incorrect")
#      print("score:=", score)

# ------------------------------------ Find two semester average of a student--------------------------------------
# Student = str(input("Enter the name:"))
# Subject = ['Math','Programming','English','Physics']
# list=[]
# n = int(input("Enter the element:"))
# for i in range(0,n):
#     ele = int(input())
#     list.append(ele)
# print(Subject)
# print(list)
# print("Percentage:=",sum(list)*100/400,"%")
# print("CGPA:=",sum(list)*100/400/9.5)
# print("\n")
#
# list1=[]
# n = int(input("Enter the element:"))
# for i in range(0,n):
#     ele = int(input())
#     list1.append(ele)
# print(Subject)
# print(list1)
# print("Percentage:=",sum(list1)*100/400,"%")
# print("CGPA:=",sum(list1)*100/400/9.5)
# print("\n")
# print("Total Aggregate Percentage of 1st SEMESTER and 2nd SEMESTER:=",sum(list+list1)*100/800,"%")
# print("Total CGPA Percentage of 1st SEMESTER and 2nd SEMESTER:=",sum(list+list1)*100/800/9.5,"CGPA")
#

# ------------------------------for multiple student storing the marks--------------------------------------
# dict={}
# for i in range(3):
#     student = input("Enter the student name:")
#     dict[student] = {}
#     English = int(input("Enter the marks of English:="))
#     Programming = int(input("Enter the marks of programming:="))
#     Math = int(input("Enter the marks of math:="))
#     Physics = int(input("Enter the marks of physics:="))
#     dict[student]["English"] = English
#     dict[student]["Programming"] = Programming
#     dict[student]["Math"] = Math
#     dict[student]["Physics"] = Physics
#     print(dict)
#     Total = English+Programming+Math+Physics
#     Maximum = max(English,Programming,Math,Physics)
#     Minimum = min(English,Programming,Math,Physics)
#     print("Maximum_marks:=",Maximum)
#     print("Minimum_marks:=",Minimum)
#     print("Total_marks:=",Total)
#     print("Percentage:=",Total*100/400,"%")
#     print(Total*100/400/9.5,"CGPA")
#     print("\n")

# ------------------------------------Costmaize House--------------------------------------

# def fun():
#     n = str(input("Enter the land area:\na. 100*100 sqf \nb. 120*180 sqf \nc. 200*250 sqf \nd. Invalid \n Chose "
#                   "options: \n "))
#     if (n == "a"):
#         print("Land price of 100*100:=", 300000)
#         Bricks = 100000
#         cement = 120000
#         others = 300000
#         Tiles = 150000
#         WallPutty = 150000
#         Wiring = 50000
#         Furnitures = 120000
#         Fans = 10000
#         Land = 300000
#         print("Bricks:=",Bricks,"\n","cement:=",cement,"\n","others:=",others,"\n","Tiles:=",Tiles,"\n","WallPutty:=",WallPutty,"\n","Wiring:=",Wiring,"\n","Furnitures:=",Furnitures,"\n",
#               "Fans:=",Fans,"\n","Land:=",Land)
#         Total =  Bricks+cement+others+Tiles+WallPutty+Wiring+Furnitures+Fans+Land
#         print("Total Price of 1BHK House:=",Total)
#
#     elif (n == "b"):
#         print("Land Price of 120*180:=", 500000)
#         Bricks = 200000
#         cement = 220000
#         others = 600000
#         Tiles = 300000
#         WallPutty = 250000
#         Wiring = 100000
#         Furnitures = 220000
#         Fans = 20000
#         Land = 600000
#         print("Bricks:=", Bricks, "\n", "cement:=", cement, "\n", "others:=", others, "\n", "Tiles:=", Tiles, "\n",
#               "WallPutty:=", WallPutty, "\n", "Wiring:=", Wiring, "\n", "Furnitures:=", Furnitures, "\n",
#               "Fans:=", Fans, "\n", "Land:=", Land)
#         Total = Bricks + cement + others + Tiles + WallPutty + Wiring + Furnitures + Fans + Land
#         print("Total Price of 2BHK House:=", Total)
#     elif (n == "c"):
#         print("Land Price of 200*250:=", 800000)
#         Bricks = 200000
#         cement = 320000
#         others = 1000000
#         Tiles = 500000
#         WallPutty = 350000
#         Wiring = 150000
#         Furnitures = 320000
#         Fans = 20000
#         Land = 800000
#         print("Bricks:=", Bricks, "\n", "cement:=", cement, "\n", "others:=", others, "\n", "Tiles:=", Tiles, "\n",
#               "WallPutty:=", WallPutty, "\n", "Wiring:=", Wiring, "\n", "Furnitures:=", Furnitures, "\n",
#               "Fans:=", Fans, "\n", "Land:=", Land)
#         Total = Bricks + cement + others + Tiles + WallPutty + Wiring + Furnitures + Fans + Land
#         print("Total Price of 3BHK House:=", Total)
#     else:
#         print("Invalid")
#
#
# fun()

# ------------------------Rolling a Dice------------------------
# import random
#
# print("1. Roll_dice  2. Exit_dice")
# user = int(input("Enter the number:="))
# if user == 1:
#     number = random.randint(1,6)
#     print(number)

# ---------------Second method--------------
# def user(user_str):
#     if user_str.strip() in {"1", "2", "3", "4", "5", "6"}:
#         return int(user_str)


# ----------------------Password Generator-----------------------------
import random

# char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678!@#$%^&*()<>?/\{}"
# while 1:
#     pass_len = int(input("Enter the password length:="))
#     pass_cont = int(input("How many password you want:="))
#     for x in range(0, pass_cont):
#         password = ""
#         for x in range(0,pass_len):
#             password_char = random.choice(char)
#             password = password_char+password
#         print("Random Password:",password)

# second method
User_name="Ravindra123"
password = "Xyz1234"
print("User_name:=",User_name)
print("Password:=",password)
user=input("Enter user_name:")
passwd = input("Enter password:")
if User_name == user:
 if password == passwd:
    print("Correct!")


    def fun():
        length = int(input("Enter the length of the password you want:"))
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678!@#$%^&*()<>?/\{}"
        x = random.sample(char, length)
        password = " ".join(x)
        print(password)
        fun()


    fun()
else:
    print("Please Enter the Correct Password")

# import random
# otp = random.randint(1000,10000)
# print(otp)
# user = int(input("Enter the number:"))
# if(user == otp):
#     first = str(input("Enter  first name: "))
#     last = str(input("Enter  last name:"))
#     Email = input("Enter the Email:")
# else:
#     print("Sorry! your otp is incorrect")
