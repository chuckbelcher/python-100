from random import choice

def get_quotes():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    return [quote.strip() for quote in quotes]

guotes = get_quotes()

selected_quote = choice(guotes)
print(selected_quote)