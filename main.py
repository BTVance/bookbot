from stats import word_in_book 
from stats import char_in_book
from stats import sort_chars
from stats import print_report
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    get_book_text = get_book_text()
    word_count = word_in_book()
    character_count = char_in_book()
    sorted_chars = sort_chars(character_count)
    print_report(word_count, sorted_chars)
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()

