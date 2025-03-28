from bs4 import BeautifulSoup
import requests
import funcAux

# Get HTML of the page with the info of each Modern Deck
# Extract each <class> with name "deck-price-online"
web_page = requests.get("https://www.mtggoldfish.com/metagame/modern/full#paper")
soup = BeautifulSoup(web_page.text, "html.parser")
decks = soup.find_all(class_="deck-price-online")

# Regex patterns
regex_expression = r'/archetype/modern-(.*?)#online'  # Extract deck name
regex_pattern_clean_name = r'-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'  # Remove full UUID (random letters we don't want)

# Variable Declarations
array_decks = []
fileName = "decks_name.txt"

funcAux.fetch_decks(decks, regex_expression, regex_pattern_clean_name, array_decks)
funcAux.add_new_decks_file_txt(fileName, array_decks)

