#
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

def addition(first_num, second_num, third_num):
    return first_num + second_num + third_num

def multiplication(first_num, second_num, third_num):
    return first_num * second_num * third_num

def average(first_num, second_num, third_num):
    return (first_num + second_num + third_num) / 3

if __name__ == "__main__":
    print(addition(first_number, second_number, third_number))
    print(multiplication(first_number, second_number, third_number))
    print(average(first_number, second_number, third_number))