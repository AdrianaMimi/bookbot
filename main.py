from stats import number_of_letters
from stats import number_of_words
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def sort_on(item):
    return item[1]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    all_letters = number_of_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"'Found {all_letters} total words'")

    result = number_of_letters(book)  
    sorted_items = sorted(result.items(), key=sort_on, reverse=True) 
    print("--------- Character Count -------")
    for letter, count in sorted_items:
        print(f"'{letter}: {count}'")
    print("============= END ===============")
    
main()