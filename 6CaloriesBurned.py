def weight_lost():
    weight_loss_formula = 454 / 3500
    total_calories = 0
    biking = int(input("Biking time: "))
    jogging = int(input("Jogging time: "))
    swimming = int(input("Swimming time: "))
    total_calories += biking * 200 + jogging * 475 + swimming * 275
    weight = total_calories * weight_loss_formula
    weight = weight / 1000
    print(f"Weight lost after {biking} hours of biking, {jogging} hours of "
          f"jogging and {swimming} hours of swimming: {weight:.3f} kgs")


weight_lost()
