import time

print("Hello and welcome to my calculator!")
time.sleep(1)
print("You can do basic, 4 function math problems with it, what do you want to do? ")
time.sleep(1)


while True:
    # asks the user for their wanted operation
    print("Chose the corresponding number to the operation. ")
    operation = int(input(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n "))

    num1 = int(input("What do you want the first number to be?: "))
    num2 = int(input("What do you want the second number to be?: "))

    # executes the correct opration
    if operation == 1:
        sum = num1 + num2
        print(f"The sum is: {sum}")
    elif operation == 2:
        difference = num1 - num2
        print(f"The difference is {difference}")
    elif operation == 3:
        product = num1 * num2
        print(f"The product is {product}")
    elif operation == 4:
        remainder = input("Assuming your quotient has a remainder, do you want it in decimal form or print the remainder?: ")
        if remainder == "decimal":
            quotient = num1 / num2
            print(f"The quotient is {quotient}")
        elif remainder == "remainder":
            quotient = int(num1 / num2)
            remainder = num1 % num2
            print(f"The quotient is {quotient} with a remainder of {remainder}")
    
    repeat = input("Do you want to run the calculator again? (y/n) ")
    if repeat == "n":
        break
