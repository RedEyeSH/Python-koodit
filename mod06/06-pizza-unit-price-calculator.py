import math

def calculation(diameter, price):
    radius = diameter / 2
    area = math.pi * radius ** 2
    square_meter = area / 10000

    return price / square_meter

if __name__ == "__main__":
    diameter_val1 = float(input("Enter first pizza's diameter in cm: "))
    price_val1 = float(input("Enter first pizza's price: "))
    diameter_val2 = float(input("Enter second pizza's diameter in cm: "))
    price_val2 = float(input("Enter second pizza's price: "))

    pizza1 = calculation(diameter_val1, price_val1)
    pizza2 = calculation(diameter_val2, price_val2)

    print(f"Pizza 1 price per square meter: {pizza1:.2f} euros/m²")
    print(f"Pizza 2 price per square meter: {pizza2:.2f} euros/m²")

    if pizza1 < pizza2:
        print("Pizza 1 provides better value for money.")
    elif pizza2 < pizza1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide better value for money.")