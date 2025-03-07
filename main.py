from stats import (
    get_num_of_words, 
    get_num_of_chars, 
    get_sorted_list
    )
import sys

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    # file_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_of_words(book_text)
    num_chars = get_num_of_chars(book_text)
    chars_sorted_list = get_sorted_list(num_chars)
    print_report(file_path, num_words, chars_sorted_list)

def print_report(file_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
   
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


main()



