import random
import json

# Define the path to the quotes JSON file
QUOTES_FILE = "quotes.json"

def load_quotes():
    try:
        with open(QUOTES_FILE, "r") as file:
            quotes = json.load(file)
    except FileNotFoundError:
        quotes = {}
    return quotes

def save_quotes(quotes):
    with open(QUOTES_FILE, "w") as file:
        json.dump(quotes, file, indent=4)

def get_user_input(prompt, options):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= len(options):
                return user_input
            else:
                print("Invalid input. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_quote(quotes):
    category = input("Enter the category for the new quote: ")
    quote = input("Enter the new quote: ")

    if category in quotes:
        quotes[category].append(quote)
        print("Quote added successfully!")
    else:
        quotes[category] = [quote]
        print("New category and quote added successfully!")

# Load quotes from the JSON file
quotes = load_quotes()

# Prompt the user for their name
name = input("Enter your name: ")

while True:
    # Prompt the user to select a category or add their own quote
    print("Select a category:")
    categories = list(quotes.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")
    print(f"{len(categories) + 1}. Add your own quote")
    print(f"{len(categories) + 2}. Exit")

    category_num = get_user_input("Enter the category number: ", categories + ["add", "exit"])

    if category_num == len(categories) + 1:
        add_quote(quotes)
        save_quotes(quotes)

        # Retrieve a random quote from the newly added category
        selected_category = category
        quote = random.choice(quotes[selected_category])
    elif category_num == len(categories) + 2:
        print("Exiting the program...")
        break
    else:
        selected_category = categories[category_num - 1]

        # Retrieve a random quote from the selected category
        quote = random.choice(quotes[selected_category])

    # Personalize the quote with the user's name
    personalized_quote = quote.replace("{name}", name)

    # Display the personalized quote
    print(f"\n{personalized_quote}")
