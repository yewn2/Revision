def storm_distance():
    time = float(input("How many seconds between the lightning and the "
                       "thunder? "))
    distance = time * 0.340
    print(f"The storm is {distance:.2f} km away.")


storm_distance()
