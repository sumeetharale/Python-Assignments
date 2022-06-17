# this is program to find if given number is armstrong number


from cgi import test


def armstrong_number(number):
    string_no = str(number)
    total_digit = len(string_no)
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit ** total_digit
        number = number // 10
    return sum
    


print("Welcome to armstrong number test")
number = int(input("Enter the number:"))

result = armstrong_number(number)
if number == result:
    print("Great ! {} is an armstrong number".format(number))
else:
    print("Ohhh.. {} this number is not armstrong number".format(number))