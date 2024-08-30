seasons = ("winter", "spring", "summer", "autumn")

months = {1: "January",
          2: "February",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
          10: "October",
          11: "November",
          12: "December"}

while True:
    user_input = input("Enter a month (1-12): ")

    try:
        user_input = int(user_input)
        if 1 <= user_input <= 12:
            break
        else:
            print("Invalid month!")
    except ValueError:
        print("Please enter a valid number!")

month_index = (user_input % 12) // 3

print("Your input:", user_input)
print("Month:", months[user_input])
print("Season:", seasons[month_index])

