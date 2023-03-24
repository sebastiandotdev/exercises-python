# Arimethics
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


if __name__ == '__main__':
    number_one = int(input("ingresa un numero: "))
    number_two = int(input("ingresa un numero: "))

    add, subtract, multiply = number_one + \
        number_two, number_one - number_two, number_one * number_two

    print(f"suma: {add}, resta: {subtract}, multiplicacion: {multiply}")