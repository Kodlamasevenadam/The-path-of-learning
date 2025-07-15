unit = input("cantimetre or meter (cm or m)")


lenght = input("Lenght:")
width = input("width:")
lenght = int(lenght)
width = int(width)
Area = (lenght * width)
Area = int(Area)

if unit == "cm":
    Area = Area / 100
elif unit == "m":
    Area = "Area"


print(f"Area of your rectangle is {Area} metersquare ")
