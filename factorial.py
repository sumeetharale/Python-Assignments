# this is program to calculate factorial
# Program implemented using iterative method

def factorial(number):
    if number == 0:
        return 1
    f = 1
    for i in range(number):
        f = f * number
        return f

print("Welcome to Factorial Program")
number = int(input("Enter the number:"))

fact = factorial(number)
print("Factorial of {} is {}".format(number, fact))