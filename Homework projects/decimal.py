def binary_to_decimal(binary_string):
    return int(binary_string, 2)

if __name__ == "__main__":
    user_input = input()
    decimal_value = binary_to_decimal(user_input)
    print(decimal_value)