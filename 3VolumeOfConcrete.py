import sys


def concrete_volume():
    keep_going = True
    total = 0
    while keep_going:
        inputs = input("Enter the building type, length and width, "
                       "separated by a comma and space. ")
        building, length, width = inputs.split(", ")
        building = building.lower()
        length = int(length)
        width = int(width)
        if building == "x":
            print(f"The total volume of concrete required for the day is "
                  f"{total} cubic metres.")
            sys.exit()
        elif building == "residential":
            depth = 0.25
            volume = depth * length * width
            total += volume
            print("The volume of concrete required for a concrete slab with a "
                  f"length of {length} metres and a width of {width} metres "
                  f"and a depth of {depth} metres is {volume} cubic metres.")
        elif building == "commercial":
            depth = 0.5
            volume = depth * length * width
            total += volume
            print("The volume of concrete required for a concrete slab with a "
                  f"length of {length} metres and a width of {width} metres "
                  f"and a depth of {depth} metres is {volume} cubic metres.")


concrete_volume()
