# # app.py

# import math
# my_name = "Tanimara"
# print("Hello and welcome " + my_name + "!")

# # this is how to write a comment

# print("*" * 10)

# print(2 + 3)

# x = 1

# print(len(my_name))
# print(my_name[0])
# print(my_name[0:3])
# print(my_name[0:])
# print(my_name[:3])
# print(my_name[:])

# # Escape sequences

# # \""
# # \'
# # \\
# # \n
# course = "Python \"Programming"
# print(course)

# # Concatenation

# my_last_name = "Elias"

# full = f"{my_name} {my_last_name}"

# print(full)

# # Methods
# course = "   Python Programming"
# # print everything in uppercase
# print(course.upper())
# # print everything in lowercase
# print(course.lower())
# # print every word titlecased
# print(course.title())
# # removes space (lstrip for spaces to the left, rstrip for spaces to the right)
# print(course.strip())
# # finds characters index
# print(course.find("Pro"))
# # finds and replaces characters
# print(course.replace("P", "j"))
# # finds and shows boolean for characters
# print("Pro" in course)
# # finds and shows bollean for characters that are not on variable
# print("swift" not in course)

# # Video is here: https://www.youtube.com/watch?v=K5KVEU3aaeQ&t=691s
# # I've stopped at the 54:00 mark.

# # Numbers
# # Three types of numbers: integers, floats, complex numbers.

# x = 1
# x = 1.1
# x = 1 + 2j  # a + bi

# # Math operations
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# # if we need an integer for the result of the division we use two slashes
# print(10 // 3)
# print(10 % 3)
# # exponent operator
# print(10 ** 3)

# # augmented assignment operator
# x = 10
# x = x + 3
# x = + 3


# # Functions to work with numbers
# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))

# # x = input(" x: ")
# # # y = x + 1
# # #Error when running code because two objects are differently typed.
# # print(type(x))

# # #Fixing the error
# # y = int(x) + 1
# # print(f"x: {x}, y: {y}")

# # Falsy values (in a boolean value it will show FALSE)
# # Empty strings " "
# # 0
# # None
# print(bool(0))

# # Primitive types in Python
# # Strings, Numbers and Booleans

# # Fundamentals of programming
# # Comparison operators
# print(10 > 3)
# print(10 >= 3)
# print(10 < 20)
# print(10 <= 20)
# print(10 == 10)
# print(10 == "10")
# print(10 != "10")
# print("bag" > "apple")
# print("bag" == "BAG")
# print(ord("b"))
# print(ord("B"))

# # Conditional statements
# temperature = 35
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# # Cleaner code
# age = 22
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)


# # Logical operators
# # and
# # high_income = True
# # good_credit = True

# # if high_income and good_credit:
# #     print("Eligible")
# # else:
# #     print("Not eligible")

# # or
# # high_income = False
# # good_credit = True

# # if high_income or good_credit:
# #     print("Eligible")
# # else:
# #     print("Not eligible")

# # not
# high_income = False
# good_credit = True
# student = True

# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# # Chaining comparison operators
# age = 22
# if age >= 18 and age < 65:
#     print("Eligible")
# # Is the same as:
# if 18 <= age < 65:
#     print("Eligible")

# Quiz: what is gonna show on the terminal?
# if 1-0 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

#Using loops
# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")
# successful = True
# for number in range(3):
#     print("attempt")
#     if successful:
#         print("Successful")
#         break
#     else:
#         print("attempted 3 times and failed")
# Loop inside a loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")
#Iterables
#Range objects
print(type(5))
print(type(range(5)))

for x in range(5):
    print(x)
#String objects
# for x in "Python":
#     print(x)