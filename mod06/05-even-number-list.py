def num(num_list):
    even_num_list = []

    for n in num_list:
        if n % 2 == 0:
            even_num_list.append(n)

    return even_num_list

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Original list:", numbers)
    print("Even numbers list from (Original list):", num(numbers))
