
# Write a python program that:
#     Asks the user about their name
#     Save it in a variable called "name"
#     Asks the user about their age
#     Save it in a variable called "age"
#     Print a string stating "The user -name- is -age- years old"
name = input("Enter your name: ")
age = input("Enter your age: ")
print("The user "+name+" is "+age+" years old.")
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
#  Extras:
# If the number is a multiple of 4, print out a different message. 

num = int(input("Enter a number: "))
if num%2==0:
    print("even")
elif num%4==0:
    print("multiple of 4")
else:
    print("odd")

    # Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.
check = int(input("Enter a chedk num: "))
num2 = int(input("Enter a number: "))
if num%check==0:
    print("divisible")
else:
    print("not divisible")

# Write a program that takes a list of numbers 
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first
# and last elements of the given list.
# For practice, write this code inside a function.

def method():
    a = [5, 10, 15, 20, 25]
    b = [a[0], a[-1]]
    print(b)

method()

# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.

def E(a,b):
    if b in a:
        return "found"
    else:
        return "not found"

print(E([1,2,3,4], 2))