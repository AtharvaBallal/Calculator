import art

print(art.logo)
first = float(input("What's the first number:"))
operation = input("+\n-\n*\n/\nPick an operation:")
second = float(input("What's the second number:"))
end = False


def add(first, second):
    return first + second


def sub(first, second):
    return first - second


def mul(first, second):
    return first * second


def div(first, second):
    return first / second


if operation == "+":
    print(f"{first} + {second} = {add(first, second)}")
elif operation == "-":
    print(f"{first} + {second} = {sub(first, second)}")
elif operation == "*":
    print(f"{first} + {second} = {mul(first, second)}")
elif operation == "/":
    print(f"{first} + {second} = {div(first, second)}")
