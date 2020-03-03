# declaring variables
age = 28
name = "Aslam"
location = "ON"
age, name, location = 28, "Aslam", "ON"
a = b = c = 1
AGE = 37
AGE = 41
userAge = age # Not convention to use camel case
user_name = "Aslam" # Convention is to use snake case
__user_location__ = "ON" # Do not change this, up in priority order of variables
print(AGE)

# Variable Conventions:
# There are no constants like in JS, every variable can be reassigned
# The variable that are meant to be constants are in capital letters, please do not reassign
# The variables are in snake case as a convention as opposed to camel case
# Variables with double underscore must not be changed, more priority than variables in uppercase, if changed can break something
# The data types of variables are not required to be mentioned for eg: int, float, string etc. This is called as dynamic typing

total_score = None
# null == None; in python
print(total_score)

username = input("What's your name?")
user_location = input ("Where do you live?")
user_age = input("How old are you?")

print(f"{username} is {user_age} years old and lives in {user_location}")
