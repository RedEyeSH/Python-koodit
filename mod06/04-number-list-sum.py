def math(num_list):
    value = 0

    for i in range(len(num_list)):
        value += num_list[i]

    return value

if __name__ == "__main__":
    numbers = [6, 24, 15, 55]
    print("The sum of the numbers in the list:", math(numbers))