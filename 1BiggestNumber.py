def biggest_number():
    two = input("Enter two numbers, separated by a space; enter the first "
                "number as '0' to cancel: ")
    a, b = two.split(" ")
    a = int(a)
    b = int(b)
    equal_statement = "Numbers equal."
    while a != 0:
        a = int(a)
        b = int(b)
        if a == b:
            print(equal_statement)
        elif a >= b:
            print(a)
        elif a <= b:
            print(b)
        two = input("Enter two numbers, separated by a space; enter the first "
                    "number as '0' to cancel: ")
        a, b = two.split(" ")


biggest_number()
