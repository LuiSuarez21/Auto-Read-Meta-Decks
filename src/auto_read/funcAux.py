import re

def add_new_decks_file_txt (fileName, array_decks):
    file = open(fileName, "w")
    for name in array_decks:
        file.write(name)
        file.write("\n")
    file.close()


def fetch_decks(decks_html, regex_expression, regex_pattern_clean_name, array_decks):
    for deck in decks_html:
        deckString = str(deck)
        result_search = re.search(regex_expression, deckString)

        if result_search:
            deck_name = result_search.group(1)
            clean_deck_name = re.sub(regex_pattern_clean_name, '', deck_name)
            array_decks.append(clean_deck_name)


def fetch_option(options_html, regex_expression, array_options):
    new_array_options = []
    for option in options_html:
        option_string = str(option)
        result_search = re.search(regex_expression, option_string)
        array_options.append(re.findall(r'[0-9]{2}', str(result_search)))

    for item in array_options:
        for it in item:
            if (int(it) == 7 or int(it) == 14 or int(it) == 30 or int(it) == 90) and it not in new_array_options:
                new_array_options.append(it)

    array_options.clear()
    array_options.extend(new_array_options)


def menu(array_decks, array_options):
    print("-----------------------------------------\n\n")
    print("Error!!! Please insert a correct value!!!")
    print("1) All decks of the current meta on Modern;")
    print("2) All decks of the current meta on Modern on the last 7 Days;")
    print("3) Prices of each deck;")
    print("4) Top 3 positions on the last competitions of this Modern Decks;")
    print("5) Give me a deck list of a certain deck;")
    option = int(input("\nChoose an option: "))

    while option in range(1, 5) == False:
        print("-----------------------------------------\n\n")
        print("Error!!! Please insert a correct value!!!")
        print("1) All decks of the current meta on Modern;")
        print("2) All decks of the current meta on Modern on the last 7 Days;")
        print("3) Prices of each deck;")
        print("4) Top 3 positions on the last competitions of this Modern Decks;")
        print("5) Give me a deck list of a certain deck;")
        option = int(input("\nChoose an option: "))

    match option:
        case 1:
            show_all_decks(array_decks)

        case 2:
            print("Function not completed...")
            breakpoint()

        case 3:
            print("Function not completed...")
            breakpoint()

        case 4:
            print("Function not completed...")
            breakpoint()

        case 5:
            print("Function not completed...")
            breakpoint()


def show_all_decks(array_decks):
    print("\n----------------------------")
    print("All decks on the current Modern Format:\n")
    for element in array_decks:
        print(element)