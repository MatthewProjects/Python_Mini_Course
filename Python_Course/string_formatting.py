def main():
  name = "Matt"
  age = 25
  country = "USA"
  city = "Boulder"
  language1 = "English"
  language2 = "Portuguese"

  # Define the quote variable
  quote = "The only limit to our realization of tomorrow is our doubts of today."

  # Print the initial information
  print(f"My name is {name}, I'm {age} years old, and I live in {city}, {country}. I speak {language1} & {language2}.")

  # Print the quote with escape characters using f-string
  print(f'In {country}, people say:\n\t"{quote}"')

if __name__ == "__main__":
  main()
