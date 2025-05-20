import pytest
from src.auto_read.funcAux import add_new_decks_file_txt, fetch_decks, fetch_option, show_all_decks


# ------------------------------
# Test for add_new_decks_file_txt
# ------------------------------
def test_add_new_decks_file_txt(tmp_path):
    decks = ["Deck One", "Deck Two"]
    file_path = tmp_path / "decks.txt"

    add_new_decks_file_txt(file_path, decks)

    with open(file_path, "r") as f:
        content = f.read().strip().split("\n")
    assert content == decks

# ------------------------------
# Test for fetch_decks
# ------------------------------
def test_fetch_decks():
    html_data = [
        '<a href="/decks/modern/deckname1">Deck One</a>',
        '<a href="/decks/modern/deckname2">Deck Two</a>'
    ]
    regex_expression = r'>(.*?)<'
    regex_pattern_clean_name = r'[^\w\s]'
    array_decks = []

    fetch_decks(html_data, regex_expression, regex_pattern_clean_name, array_decks)
    assert array_decks == ["Deck One", "Deck Two"]

# ------------------------------
# Test for fetch_option
# ------------------------------
#def test_fetch_option():
#    html_data = [
#        '<option value="7">Last 7 days</option>',
#        '<option value="14">Last 14 days</option>',
#        '<option value="30">Last 30 days</option>',
#        '<option value="90">Last 90 days</option>',
#        '<option value="180">Last 180 days</option>'
#    ]
#    regex_expression = r'value="(\d+)"'
#    options = []

#    fetch_option(html_data, regex_expression, options)
#    assert options == ["7", "14", "30", "90"]


# ------------------------------
# Test for show_all_decks (capturing output)
# ------------------------------
def test_show_all_decks_output(capsys):
    test_decks = ["Deck One", "Deck Two"]
    show_all_decks(test_decks)
    captured = capsys.readouterr()
    assert "Deck One" in captured.out
    assert "Deck Two" in captured.out
