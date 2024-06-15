def main():
    print("Running casting.main()")
    apples = 5  # Change to string
    print(type(apples))

    apples = str(apples)
    print(type(apples))

    bananas = '3'  # Change to integer
    print(type(bananas))

    bananas = int(bananas)
    print(type(bananas))

    price = 2.99  # Change to integer
    print(type(price))

    price = int(price)
    print(type(price))

    is_student = True  # Change to string
    print(type(is_student))

    is_student = str(is_student)
    print(type(is_student))

    pie = '3.14'  # Change to float
    print(type(pie))

    pie = float(pie)
    print(type(pie))

    name = 'John'  # Initial non-numeric string assignment

    if name.isdigit():
        name = int(name)  # Convert the string to an integer if it contains only digits
        print(type(name))  # Prints <class 'int'>
    else:
        print("The string cannot be converted to an integer.")  # Prints a message if the string cannot be converted

    age = 42  # Change to string
    print(type(age))
    age = str(age)
    print(type(age))

    off = 1  # Change to boolean
    print(type(off))
    off = (bool(off))
    print(type(off))
    print("Finished casting.main()")

if __name__ == "__main__":
    main()

