# 4.13.3 : Greeting
# Sophia Carahaly
# 2.6.19

name = input("What is your name: ")


def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")


greeting()

# 4.13.4 : Functions and Variables
# Sophia Carahaly
# 2.14.19

x = 89


def print_something():
    x = 13
    print(x)


print_something()
print(x)


# 4.13.5 : Functions and Variables: Part Two
# Sophia Carahaly
# 2.14.19

my_variable = 3.6745


def something():
    print(my_variable + 10)


something()

# 4.13.6: Functions and Variables, Part 3
# Sophia Carahaly
# 2.18.19


def print_number(x):
    print(str(x))


print_number(12)
print_number('\n' + 'Hello World')

# 4.14.4: Name and Age
# Sophia Carahaly
# 2.18.19


def print_name_and_age(name, age):
    print("Hi, my name is ", name, " and I am ", str(age), " years old.")


print_name_and_age("Sierra", 34)
print_name_and_age("Marcus", 19)

# 4.14.5: Default Parameter Values
# Sophia Carahaly
# 2.19.19


def print_two_numbers(x, y=20):
    print('First number:', x)
    print('Second number: ' + str(y))


print_two_numbers(3, 2)
print_two_numbers(13)

# 4.14.7 : Print Multiple Times
# Sophia Carahaly
# 2.19.19


def print_multiple_times(sting, times):
    for i in range(times):
        print(sting)


print_multiple_times('Hello', 4)




# 4.14.7 : Print Multiple Times
# Sophia Carahaly
# 2.19.19


def print_multiple_times(sting, times):
    for i in range(times):
        print(sting)


print_multiple_times('Hello', 4)




# 4.14.7 : Print Multiple Times
# Sophia Carahaly
# 2.19.19


def print_multiple_times(sting, times):
    for i in range(times):
        print(sting)


print_multiple_times('Hello', 4)


# 4.16.3: Enter a Number
# Sophia Carahaly
# 2.20.19

try:
    my_number = int(input('Enter an integer: '))
    print('Your number: ' + str(my_number))
except ValueError:
    print('That was not an integer')



# 4.16.3: Enter Name and Age
# Sophia Carahaly
# 2.20.19

name = input("what is your name: ")
age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print("That was not a valid age")

print('\n''Name:', name)
print('Age:', age)

# 4.16.9: Temperature Converter
# Sophia Carahaly
# 2.20.19


def convert_cf(C):
    return 1.8 * C + 32


def convert_fc(F):
    return (F - 32) / 1.8


try:
    c = float(input('Enter a temp in C: '))
    print('In F: ', round(convert_cf(c), 2))

    f = float(input('Enter a temp in F: '))
    print('In F: ', round(convert_fc(f), 2))

except ValueError:
    print('You must enter a float')

