def grades():
    name_list = []
    mark_list = []
    name_list, mark_list = average_mark(name_list, mark_list)
    for i in range(len(name_list)):
        if 0 <= mark_list[i] <= 39:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: E")
        elif 40 <= mark_list[i] <= 49:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: D")
        elif 50 <= mark_list[i] <= 54:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: C-")
        elif 55 <= mark_list[i] <= 59:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: C")
        elif 60 <= mark_list[i] <= 64:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: C+")
        elif 65 <= mark_list[i] <= 69:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: B-")
        elif 70 <= mark_list[i] <= 74:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: B")
        elif 75 <= mark_list[i] <= 79:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: B+")
        elif 80 <= mark_list[i] <= 84:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: A-")
        elif 85 <= mark_list[i] <= 89:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: A")
        elif 90 <= mark_list[i]:
            print(f"Name: {name_list[i]}\n"
                  f"Mark: {mark_list[i]}\n"
                  f"Grade: A+")
        print()


def average_mark(all_names, all_marks):
    total_mark = 0
    again = True
    names = "y"
    marks = 0
    while again:
        name = str(input("Student name: ")).lower()
        if name == "x":
            print()
            print(f"Highest mark: {marks} - {names}")
            print()
            return all_names, all_marks
        mark = int(input("Student mark: "))
        if mark > marks:
            marks = mark
            names = name.capitalize()
            all_names.append(name.capitalize())
            all_marks.append(mark)
        total_mark += mark
        print()


grades()
