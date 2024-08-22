#print("A normal hemoglobin value for adult females is between 117-155 g/l.")
#print("A normal hemoglobin value for adult males is between 134-167 g/l.")
from lib2to3.pgen2.token import NUMBER

#biological_gender = input("Enter your Biological Gender (man/woman): ")
#hemoglobin_value = int(input("Enter your Hemoglobin value: "))

while True:
    biological_gender = input("\nEnter your Biological Gender (man/woman): ")
    if biological_gender == "man":
        break
    elif biological_gender == "woman":
        break
    else:
        print("Please enter (man or woman)")

def hemoglobin_val():
    while True:
        try:
            h_value = int(input("Enter your Hemoglobin value: "))
        except ValueError:
            print("Please enter a number")
        else:
            return h_value

hemoglobin_value = hemoglobin_val()

# Finland version amount of g/l.
# Female: 117-175 g/l.
# Male: 134-195 g/l.
if biological_gender == "man":
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin value is normal.")
    elif hemoglobin_value > 167:
        print("Your hemoglobin value is high.")
elif biological_gender == "woman":
    if hemoglobin_value < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin value is normal.")
    elif hemoglobin_value > 155:
        print("Your hemoglobin value is high.")