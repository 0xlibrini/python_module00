def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plante!")
    else:
        print("Plants are fine")