unit = input("what is the unit of measurment? (C or F):")
temp = float(input("Enter the tempereture "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"Your tempereture in F is {temp} degrece fahrenheit ")
elif unit == "F":
    print(f"Your temperature is {temp} degrece fahrenheit ")


else:
    print(
        f"Your {unit} unit is not valid please try the units that has been shown ")
