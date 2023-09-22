# Ex1
paragraph = "\n------------------------------------------------------------------------"
integer = 100
float_op = 3.14
logic = True
text = 'lorem ipsum'
print(f"{paragraph}\n Ex 1\n {integer}, {type(integer)}\n {float}, {type(float)}\n {logic}, {type(logic)}\n {text}, {type(text)} {paragraph}")

# Ex 2
print('\nEx 2')
first_num = int(input("Write first number: "))
second_num = int(input("Write second number: "))
sum = first_num + second_num
difference = first_num - second_num
division = first_num / second_num
multiplication = first_num * second_num
print (f" sum = {sum}\n difference = {difference}\n multipication = {multiplication}\n division = {division} {paragraph}")

#Ex 3
while True:
    decision = int(input("Hello, please choose what you want!\n 1. Calculator\n 2. Сomparisons\n 3. Data type conversion\n"))

    if decision == 1:
        operation = int(input("What operation do you want to do? (choose number)\n 1. +\n 2. -\n 3. *\n 4. /\n "))
        first_num = float(input('Write first number: '))
        second_num = float(input("Write second number: "))
        if operation == 1:
            result = first_num + second_num 
        elif operation == 2:
            result = first_num - second_num
        elif operation == 3:
            result = first_num * second_num
        elif operation == 4:
            result = first_num / second_num
        else:
            print("Erorrrr\n You chose the wrong option!")
    elif decision == 2:
        comparison = int(input("Enter a comparison action: \n1. Is the first number equal the second number? \n2. Is the first number less than the second number? \n3. Is The first number greater than the second?\n"))
        first_num = float(input("Write first number: "))
        second_num = float(input("Write second number: "))
        if comparison == 1:
            comparison_equal = first_num == second_num
            if comparison_equal is True:
                result = f"{comparison_equal}. The numbers are equal!"
            elif first_num > second_num:
                result = f"{comparison_equal}. The first number is greater than the second!"
            elif first_num < second_num:
                result = f"{comparison_equal}. The first number is less than the second number"
            else:
                print("Erorrrr\n You chose the wrong option!")
        elif comparison == 2:
            comparison_less = first_num < second_num
            if comparison_less is True:
                result = f"{comparison_less}. The first number is less than the second number"
            elif first_num > second_num:
                result = f"{comparison_less}. The first number is greater than the second!"
            elif first_num == second_num:
                result = f"{comparison_less}. The numbers are equal!"
            else:
                print("Erorrrr\n You chose the wrong option!")
        elif comparison == 3:
            comparison_greater = first_num > second_num
            if comparison_greater is True:
                result = f"{comparison_greater}. The first number is greater than the second!"
            elif first_num < second_num:
                result = f"{comparison_greater}. The first number is less than the second number"
            elif first_num == second_num:
                result = f"{comparison_greater}. The numbers are equal!"
            else:
                print("Erorrrr\n You chose the wrong option!")        
        else:
            print("Erorrrr\n You chose the wrong option!") 
    elif decision == 3:
        value = input("What value you want to convert? ")
        convert_type = int(input("Choose type to convert: \n 1. integer\n 2. float\n 3. string\n"))
        if convert_type == 1:
            result = int(value)
        elif convert_type == 2:
            result = float(value)
        elif convert_type == 3:
            result = str(value)
        else:
            print("Erorrrr\n You chose the wrong option!")
    print(f"Result: {result} {paragraph}")  

    repeat = input("Do you want to repeat the program? \n(yes/no): ")
    if repeat.lower() != "yes":
        break