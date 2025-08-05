# app.py

my_name = "Tanimara"
print("Hello and welcome " + my_name + "!")

# this is how to write a comment

print("*" * 10)

print(2 + 3)

x = 1

print(len(my_name))
print(my_name[0])
print(my_name[0:3])
print(my_name[0:])
print(my_name[:3])
print(my_name[:])

# Escape sequences

# \""
# \'
# \\
# \n
course = "Python \"Programming"
print(course)

# Concatenation

my_last_name = "Elias"

full = f"{my_name} {my_last_name}"

print(full)

# Methods
course = "   Python Programming"
# print everything in uppercase
print(course.upper())
# print everything in lowercase
print(course.lower())
# print every word titlecased
print(course.title())
# removes space (lstrip for spaces to the left, rstrip for spaces to the right)
print(course.strip())
# finds characters index
print(course.find("Pro"))
# finds and replaces characters
print(course.replace("P", "j"))
# finds and shows boolean for characters
print("Pro" in course)
# finds and shows bollean for characters that are not on variable
print("swift" not in course)

#Video is here: https://www.youtube.com/watch?v=K5KVEU3aaeQ&t=691s
#I've stopped at the 54:00 mark.