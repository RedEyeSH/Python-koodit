talent = float(input("Enter talents: \n"))
pound = float(input("\nEnter pounds: \n"))
lot = float(input("\nEnter lots: \n"))

def calculate(talents, pounds, lots):
    total_pounds = talents * 20 + pounds # Converting talents to pounds by 20 (One talent is 20 pounds)
    total_lots = total_pounds * 32 # Converting pounds to lots by 32 (One pound is 32 lots)
    total_grams = (total_lots + lots) * 13.3 # Converting lots to grams by 13.3 (One lot is 13.3 grams)

    # Another way to calculate with less code
    # total_grams = ((talents * 20 + pounds) * 32 + lots) * 13.3

    # Calculating kilograms and grams
    remaining_kilograms = total_grams // 1000
    remaining_grams = total_grams % 1000

    return remaining_kilograms, remaining_grams

def result():
    kilograms, grams = calculate(talent, pound, lot)

    print("\nThe weight in modern units: ")
    print(f"{int(kilograms)} kilograms and {grams:.2f} grams.")

if __name__ == "__main__":
    result()