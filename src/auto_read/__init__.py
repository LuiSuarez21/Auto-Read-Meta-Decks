from bs4 import BeautifulSoup
from src.auto_read import funcAux
import requests


def main():
    # Get HTML of the page with the info of each Modern Deck
    # Extract each <class> with name "deck-price-online"
    web_page = requests.get("https://www.mtggoldfish.com/metagame/modern/full#paper")
    soup = BeautifulSoup(web_page.text, "html.parser")
    decks_html = soup.find_all(class_="deck-price-online")
    option_html = soup.find_all(class_="metagame-re-sort")

    # Regex patterns
    regex_expression = r'/archetype/modern-(.*?)#online'  # Extract deck name
    regex_expression_option_selected = r'<option selected="selected".+'
    regex_pattern_clean_name = r'-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'  # Remove full UUID (random letters we don't want)

    # I need now to parse my option on 7 days
    # And I need, probably, to clean the excessive lines of code that will comi with this fecth

    # Variable Declarations
    array_decks = []
    array_options = []
    fileName = "../src_files/decks_name.txt"

    funcAux.fetch_decks(decks_html, regex_expression, regex_pattern_clean_name, array_decks)
    funcAux.fetch_option(option_html, regex_expression_option_selected, array_options)
    funcAux.add_new_decks_file_txt(fileName, array_decks)
    funcAux.menu(array_decks, array_options)

if __name__ == "__main__":
    main()