def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

print("Welcome to Factorial Program")
number = int(input("Enter the number:"))

fact = factorial(number)
print("Factorial of {} is {}".format(number, fact))