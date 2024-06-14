name = "John"
food = "Pizza"
age = 30
weight = 75.5
is_student = True
city = "Paris"
year = 2020
is_raining = True
price = 19.99
product_name = "Chocolate Chip Cookies"
quantity_available = 24
price_per_unit = 2.99
is_in_stock = True

print(type(name))
print(type(food))
print(type(weight))
print(type(is_student))
print(type(city))
print(type(year))
print(type(is_raining))
print(type(price))
print(type(product_name))
print(type(quantity_available))
print(type(price_per_unit))
print(type(is_in_stock))


apples = 5 # Change to string
print(type(apples))

apples = str(apples)
print(type(apples))



bananas = '3' # Change to integer
print(type(bananas))

bananas = int(bananas)
print(type(bananas))


price = 2.99 # Change to integer
print(type(price))

price = int(price)
print(type(price))




is_student = True # Change to string
print(type(is_student))

is_student = str(is_student)
print(type(is_student))


pie = '3.14' # Change to float
print(type(pie))

pie = float(pie)
print(type(pie))


name = 'John'  # Initial non-numeric string assignment

if name.isdigit():
    name = int(name)  # Convert the string to an integer if it contains only digits
    print(type(name))  # Prints <class 'int'>
else:
    print("The string cannot be converted to an integer.")  # Prints a message if the string cannot be converted



age = 42 # Change to string
print(type(age))
age = str(age)
print(type(age))



off = 1 # Change to boolean
print(type(off))
off = (bool(off))
print(type(off))



favorite_color = "blue"
print(favorite_color)

favorite_color = "purple"
print(favorite_color)



course_description = "The Python course is a comprehensive and hands-on learning experience designed to introduce students to the fundamentals of Python programming. Through a combination of interactive lectures, practical exercises, and real-world projects, participants will gain a solid understanding of Python syntax, data structures, control flow, functions, and object-oriented programming. They will also explore various libraries and modules for tasks such as data analysis, web scraping, and GUI development. By the end of the course, students will be equipped with the skills to develop their own Python applications and confidently pursue further programming endeavors"

print(len(course_description))

words = course_description.split()

print(len(words))

sentences = course_description.split(". ")

num_sentences = len(sentences)

print("Number of sentences:", num_sentences)


new_course_description = "The Python course is a comprehensive and hands-on learning experience designed to introduce students to the fundamentals of Python programming. Through a combination of interactive lectures, practical exercises, and real-world projects, participants will gain a solid understanding of Python syntax, data structures, control flow, functions, and object-oriented programming. They will also explore various libraries and modules for tasks such as data analysis, web scraping, and GUI development. By the end of the course, students will be equipped with the skills to develop their own Python applications and confidently pursue further programming endeavors"

# Replace "Python" with "JavaScript" and store the result
javascript_description = new_course_description.replace("Python", "JavaScript")

# Replace "programming" with "coding" in the modified string
modified_description = javascript_description.replace("programming", "coding")

print(modified_description)

print(modified_description.upper())

print(modified_description.lower())

