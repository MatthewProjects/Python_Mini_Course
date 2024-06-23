def main():
    # Create two variables, num1 and num2, and assign them with numeric values
    num1 = 2
    num2 = 6

    # Perform the arithmetic operations
    sum_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2
    div_result = num1 / num2
    int_div_result = num1 // num2
    mod_result = num1 % num2
    exp_result = num1 ** num2

    # Calculate the remainder of num2 divided by num1
    even_number = num2 % num1

    # Calculate the remainder of 11 divided by num1
    odd_number = 11 % num1

    # Calculate the average of given numbers
    numbers = [1, 12, 31, 14, 51, num1, num2]
    avg_result = sum(numbers) / len(numbers)

    # Print the results
    print("sum_result:", sum_result)
    print("sub_result:", sub_result)
    print("mul_result:", mul_result)
    print("div_result:", div_result)
    print("int_div_result:", int_div_result)
    print("mod_result:", mod_result)
    print("exp_result:", exp_result)
    print("even_number:", even_number)
    print("odd_number:", odd_number)
    print("avg_result:", avg_result)

if __name__ == "__main__":
    main()
