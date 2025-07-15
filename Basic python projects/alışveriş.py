# Alıjverij programı

foods = []
prices = []
total = 0


while True:
    food = input("Enter the food you want to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}:"))
        foods.append(food)
        prices.append(price)


print("Your cart:")

for food in foods:
    print(food)


for price in prices:
    total += price

print(f"your total is :{total} $")
