import sys # provides access to command line arguments
from stats import (
                    get_num_words, 
                    get_num_chars, 
                    get_chars_sorted_list
    )
# Entry function
def main():
    if len(sys.argv) != 2: # sys.argv have two arguments
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit the program   
    # Before, path_to_file = "books/frankenstein.txt" 
    path_to_file = sys.argv[1] # sys.argv[1] is the second argument as path to the book file.
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_sorted_list = get_chars_sorted_list(chars_dict)
    print_report(path_to_file, num_words, chars_sorted_list)
# Read contents of the file into a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# Print reports
def print_report(path_to_file, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for key in chars_sorted_list:  
        if not key['char'].isalpha(): 
            continue      
        print(f"{key['char']}: {key['num']}") # prints alphabetical character and character count    
    print("============= END ===============")
# Call main method last      
main() 


