# constants
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062


def area_volume():
    radius = float(input("What is the radius of the sphere? "))
    area = 4 * PI * radius * radius
    volume = 4 / 3 * PI * radius * radius * radius
    print(f"The surface area of the sphere with radius {radius}cm is\n"
          f"{area:.2f} square centimetres.\n"
          f"The volume of the sphere with radius {radius}cm is\n"
          f"{volume:.2f} cubic centimetres.")


area_volume()
