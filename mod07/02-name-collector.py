names = set()

while True:
    name = input("Enter name: ")

    if name == "":
        break
    else:
        if name not in names:
            names.add(name)
            print("New name")
        else:
            print("Existing name")

for n in names:
    print(n)