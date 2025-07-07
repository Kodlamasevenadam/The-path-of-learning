principle = 0

rate = 0

time = 0
# principle
while principle <= 0:

    principle = float(input("Enter the principle amount:"))

if principle <= 0:
    print("principle cant be 0 or less than 0 ")


# rate
while rate <= 0:

    rate = float(input("Enter the rate of interest amount:"))

if rate <= 0:
    print("rate cant be 0 or less than 0 ")


# time
while time <= 0:

    time = int(input("Enter the time amount:"))

if time <= 0:
    print("time cant be 0 or less than 0 ")


total = principle * pow((1 + rate / 100), time)

print(f"Balance after the {time} years will be {total}")
