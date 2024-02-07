import sys


def average_mark():
    total_mark = 0
    again = True
    names = "y"
    marks = 0
    while again:
        name = str(input("Student name: ")).lower()
        if name == "x":
            print(f"Highest mark: {marks} - {names}")
            sys.exit()
        mark = int(input("Student mark: "))
        if mark > marks:
            marks = mark
            names = name.capitalize()
        total_mark += mark
        print()


average_mark()
