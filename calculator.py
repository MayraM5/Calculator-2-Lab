"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def quit():
    return exit()

while True:
    input_equation = input("Enter your equation -> ")
    tokens = input_equation.split(' ')

    if tokens[0] == 'q':
        print(quit())
 
    else:
        num1 = float(tokens[1])
        try:
            num2 = float(tokens[2])
        except IndexError:
            pass
        
        if tokens[0] == '+':
            print(add(num1, num2)) 
        elif tokens[0] == '-':
            print(subtract(num1, num2))
        elif tokens[0] == '*':
            print(multiply(num1, num2))
        elif tokens[0] == '/':
            print(divide(num1, num2))
        elif tokens[0] == 'pow':
            print(power(num1, num2))
        elif tokens[0] == 'mod':
            print(mod(num1, num2))
        elif tokens[0] == 'square':
            print(square(num1))
        elif tokens[0] == 'cube':
            print(cube(num1))