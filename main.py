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
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = word_in_book(book_text)
    character_count = char_in_book(book_text)
    sorted_chars = sort_chars(character_count)
    print_report(word_count, sorted_chars)
main()

