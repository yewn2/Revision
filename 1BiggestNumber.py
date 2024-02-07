def biggest_number():
    play_on = True
    a = int(input("What is your first number? "))
    b = int(input("What is your second number? "))
    equal_statement = "Numbers equal."
    while play_on:
        if a == b:
            print(equal_statement)
        elif a >= b:
            print(f"The higher number is {a}")
        elif a <= b:
            print(f"The higher number is {b}")
        a = int(input("What is your first number? "))
        b = int(input("What is your second number? "))
        if a == 0 or b == 0:
            play_on = False


biggest_number()
