num1 = 5
num2 = -12.3
is_num1_larger = num1 > num2
word = "pizza"
is_a_in_word = "a" in word
is_o_in_word = "o" in word
is_u_in_word = "u" in word
is_num1_not_equal_to_num2 = num1 != num2

print(is_num1_larger)
print(is_a_in_word)
print(is_o_in_word)
print(is_u_in_word)
print(is_num1_not_equal_to_num2)

# Comparisons
print(5 == 5.0)       # True: Integer 5 is equal to float 5.0
print(5 != 5.0)       # False: Integer 5 is equal to float 5.0
print(5 == '5')       # False: Integer 5 is not equal to string '5'
print([] != ())       # True: Empty list is not equal to empty tuple
print([] == "")       # False: Empty list is not equal to empty string
print([] == [])       # True: Empty list is equal to empty list
print({} == {})       # True: Empty dictionary is equal to empty dictionary
print({} == ())       # False: Empty dictionary is not equal to empty tuple
print({} == 0)        # False: Empty dictionary is not equal to integer 0
